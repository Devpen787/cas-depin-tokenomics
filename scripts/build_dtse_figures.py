#!/usr/bin/env python3
import json
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path('/Users/devinsonpena/Desktop/Files/cas-depin-tokenomics')
EXPORT_ROOT = ROOT / 'exports' / 'dtse'
TABLES = EXPORT_ROOT / 'tables'
FIGS = EXPORT_ROOT / 'figures'
FIGS.mkdir(parents=True, exist_ok=True)

weekly = pd.read_csv(TABLES / 'dtse_weekly_summary.csv')
final = pd.read_csv(TABLES / 'dtse_final_summary.csv')
signals = pd.read_csv(TABLES / 'dtse_cross_scenario_signals_ono.csv')

ONO = 'ono_v3_calibrated'


def series_df(profile_id: str, scenario_id: str, metric: str) -> pd.DataFrame:
    out = weekly[
        (weekly['profile_id'] == profile_id)
        & (weekly['scenario_id'] == scenario_id)
        & (weekly['metric'] == metric)
    ][['week', 'median', 'p25', 'p75']].sort_values('week')
    return out


def plot_line_with_band(ax, df: pd.DataFrame, label: str, color: str):
    ax.plot(df['week'], df['median'], label=label, color=color, linewidth=2.4)
    ax.fill_between(df['week'], df['p25'], df['p75'], color=color, alpha=0.2)


plt.rcParams.update({
    'figure.figsize': (10.5, 4.0),
    'figure.titlesize': 15,
    'axes.titlesize': 13,
    'axes.labelsize': 11.5,
    'xtick.labelsize': 10.5,
    'ytick.labelsize': 10.5,
    'legend.fontsize': 10,
    'legend.title_fontsize': 10,
    'axes.grid': True,
    'grid.alpha': 0.25,
    'lines.linewidth': 2.4,
})

# 1 Baseline price/providers
fig, axes = plt.subplots(1, 2, figsize=(13.4, 4.0))
plot_line_with_band(axes[0], series_df(ONO, 'baseline_neutral', 'price'), 'Median (IQR)', '#1f77b4')
axes[0].annotate('PRICE DISCOVERY DECAY', xy=(15, 0.005), xytext=(25, 0.05),
                 arrowprops=dict(facecolor='#1f77b4', edgecolor='#1f77b4', arrowstyle='wedge,tail_width=0.7', alpha=0.8),
                 color='#1f77b4', weight='bold')
axes[0].set_title('Baseline (ONO): Price Signal')
axes[0].set_xlabel('Week')
axes[0].set_ylabel('Modeled Price (USD)')
axes[0].legend()
plot_line_with_band(axes[1], series_df(ONO, 'baseline_neutral', 'providers'), 'Median (IQR)', '#ff7f0e')
axes[1].annotate('BASELINE CHURN', xy=(15, 1000), xytext=(30, 2000),
                 arrowprops=dict(facecolor='#ff7f0e', edgecolor='#ff7f0e', width=2, headwidth=8),
                 color='#ff7f0e', weight='bold')
axes[1].set_title('Baseline (ONO): Active Providers')
axes[1].set_xlabel('Week')
axes[1].set_ylabel('Providers')
axes[1].legend()
fig.suptitle('BASELINE NEUTRAL (Reference Trajectories)', weight='bold')
fig.tight_layout()
fig.savefig(FIGS / 'fig_baseline_ono_price_providers.png', dpi=220, bbox_inches='tight')
plt.close(fig)

# 2 Baseline burn vs mint
fig, ax = plt.subplots(figsize=(11.2, 4.0))
df_burned = series_df(ONO, 'baseline_neutral', 'burned')
peak_burn_week = df_burned.loc[df_burned['median'].idxmax(), 'week']
peak_burn_val = df_burned['median'].max()
plot_line_with_band(ax, series_df(ONO, 'baseline_neutral', 'minted'), 'Minted', '#d62728')
plot_line_with_band(ax, df_burned, 'Burned', '#2ca02c')
ax.annotate('LATE-STAGE UTILITY SPIKE', xy=(peak_burn_week, peak_burn_val), xytext=(peak_burn_week-20, peak_burn_val*0.85),
            arrowprops=dict(facecolor='#2ca02c', edgecolor='#2ca02c', width=2, headwidth=8),
            color='#2ca02c', weight='bold', ha='center')
ax.set_title('Baseline (ONO): Emissions vs Sinks')
ax.set_xlabel('Week')
ax.set_ylabel('Tokens / week')
ax.legend()
fig.suptitle('BASELINE NEUTRAL (Emissions vs Sinks)', weight='bold')
fig.tight_layout()
fig.savefig(FIGS / 'fig_baseline_ono_burn_mint.png', dpi=220, bbox_inches='tight')
plt.close(fig)

# 3 Demand contraction vs baseline (utilisation, burn, profit)
fig, axes = plt.subplots(1, 3, figsize=(16.6, 4.0))
for i, metric, title, ylab in [
    (0, 'utilisation', 'Utilisation', '%'),
    (1, 'burned', 'Burned (Sinks)', 'Tokens / week'),
    (2, 'profit', 'Provider Profit', 'USD / week'),
]:
    b = series_df(ONO, 'baseline_neutral', metric)
    s = series_df(ONO, 'demand_contraction', metric)
    axes[i].plot(b['week'], b['median'], label='Baseline', color='#1f77b4', linewidth=2)
    axes[i].plot(s['week'], s['median'], label='Demand contraction', color='#d62728', linewidth=2)
    axes[i].set_title(title)
    axes[i].set_xlabel('Week')
    axes[i].set_ylabel(ylab)
    if i == 0:
        axes[i].axvline(12, color='#d62728', linestyle=':', linewidth=2, alpha=0.8)
        axes[i].text(13, axes[i].get_ylim()[1]*0.4, 'UTILIZATION BREAKS (W12)', color='#d62728', weight='bold', fontsize=10, va='center')
        axes[i].legend()
    elif i == 1:
        axes[i].annotate('LAG: PARTICIPATION IS STICKY', xy=(25, axes[i].get_ylim()[1]*0.5), ha='center', va='center', color='#1f77b4', weight='bold', bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="#1f77b4", lw=1.5))
    elif i == 2:
        axes[i].axvline(49, color='#d62728', linestyle=':', linewidth=2, alpha=0.8)
        axes[i].annotate('PROVIDERS EXIT (W49)', xy=(49, axes[i].get_ylim()[1]*0.5), xytext=(25, axes[i].get_ylim()[1]*0.5),
                         arrowprops=dict(facecolor='#d62728', edgecolor='#d62728', width=2, headwidth=8),
                         color='#d62728', weight='bold', va='center', ha='center')
fig.suptitle('SCENARIO A: DEMAND CONTRACTION (Reward-Demand Decoupling)', weight='bold')
fig.tight_layout()
fig.savefig(FIGS / 'fig_demand_contraction_ono_core.png', dpi=220, bbox_inches='tight')
plt.close(fig)

# 4 Liquidity shock price/churn
fig, axes = plt.subplots(1, 2, figsize=(13.6, 4.0))
for ax, metric, title, ylab, color in [
    (axes[0], 'price', 'Price Signal', 'USD', '#9467bd'),
    (axes[1], 'churnCount', 'Churn Count', 'Providers/week', '#8c564b'),
]:
    b = series_df(ONO, 'baseline_neutral', metric)
    s = series_df(ONO, 'liquidity_shock', metric)
    ax.plot(b['week'], b['median'], label='Baseline', color='#1f77b4', linewidth=2)
    ax.plot(s['week'], s['median'], label='Liquidity shock', color=color, linewidth=2)
    if metric == 'price':
        ax.axvline(20, color='#1f77b4', linestyle='--', linewidth=2.5, alpha=0.8)
        ax.text(21, ax.get_ylim()[1]*0.95, 'EVENT WEEK 20 (35% UNLOCK SHOCK)', color='#1f77b4', weight='bold', fontsize=10)
    elif metric == 'churnCount':
        ax.axvline(20, color='#1f77b4', linestyle='--', linewidth=2.5, alpha=0.8)
        max_churn = s['median'].max()
        ax.annotate('INSTANT CHURN SPIKE', xy=(20, max_churn), xytext=(26, max_churn*0.8),
                    arrowprops=dict(facecolor='#8c564b', edgecolor='#8c564b', arrowstyle='wedge,tail_width=0.7', alpha=0.8),
                    color='#8c564b', weight='bold', fontsize=11)
    ax.set_title(title)
    ax.set_xlabel('Week')
    ax.set_ylabel(ylab)
    ax.legend()
fig.suptitle('SCENARIO B: LIQUIDITY SHOCK TRANSMISSION (Liquidity-Driven Compression)', weight='bold')
fig.tight_layout()
fig.savefig(FIGS / 'fig_liquidity_shock_ono_price_churn.png', dpi=220, bbox_inches='tight')
plt.close(fig)

# 5 Competitive yield pressure
fig, axes = plt.subplots(1, 2, figsize=(13.6, 4.0))
for ax, metric, title, ylab, color in [
    (axes[0], 'providers', 'Active Providers', 'Providers', '#ff7f0e'),
    (axes[1], 'churnCount', 'Churn', 'Providers/week', '#d62728'),
]:
    b = series_df(ONO, 'baseline_neutral', metric)
    s = series_df(ONO, 'competitive_yield_pressure', metric)
    ax.plot(b['week'], b['median'], label='Baseline', color='#1f77b4', linewidth=2)
    ax.plot(s['week'], s['median'], label='Competitive yield', color=color, linewidth=2)
    if metric == 'providers':
        ax.axvline(10, color='#ff7f0e', linestyle='-', linewidth=2.5, alpha=0.8)
        ax.annotate('IMMEDIATE DIVERGENCE', xy=(10, b['median'].max()*0.5), xytext=(20, b['median'].max()*0.5),
                    arrowprops=dict(facecolor='#ff7f0e', edgecolor='#ff7f0e', width=2, headwidth=8),
                    color='#ff7f0e', weight='bold', va='center')
    elif metric == 'churnCount':
        max_churn = s['median'].max()
        max_churn_week = s.loc[s['median'].idxmax(), 'week']
        ax.annotate('OPPORTUNITY COST EXIT', xy=(max_churn_week, max_churn), xytext=(max_churn_week+6, max_churn*0.9),
                    arrowprops=dict(facecolor='#d62728', edgecolor='#d62728', width=2, headwidth=8),
                    color='#d62728', weight='bold', fontsize=11, ha='left')
    ax.set_title(title)
    ax.set_xlabel('Week')
    ax.set_ylabel(ylab)
    ax.legend()
fig.suptitle('SCENARIO C: COMPETITIVE YIELD PRESSURE (Elastic Provider Exit)', weight='bold')
fig.tight_layout()
fig.savefig(FIGS / 'fig_competitive_yield_ono_retention_churn.png', dpi=220, bbox_inches='tight')
plt.close(fig)

# 6 Cost inflation profit/providers
fig, axes = plt.subplots(1, 2, figsize=(13.6, 4.0))
for ax, metric, title, ylab, color in [
    (axes[0], 'profit', 'Provider Profit', 'USD/week', '#d62728'),
    (axes[1], 'providers', 'Active Providers', 'Providers', '#ff7f0e'),
]:
    b = series_df(ONO, 'baseline_neutral', metric)
    s = series_df(ONO, 'provider_cost_inflation', metric)
    ax.plot(b['week'], b['median'], label='Baseline', color='#1f77b4', linewidth=2)
    ax.plot(s['week'], s['median'], label='Cost inflation', color=color, linewidth=2)
    if metric == 'profit':
        ax.axhline(0, color='black', linestyle='--', linewidth=1.5, alpha=0.5)
        zero_cross = s[s['median'] <= 0]
        if not zero_cross.empty:
            cross_week = zero_cross.iloc[0]['week']
            ax.axvline(cross_week, color='#d62728', linestyle=':', linewidth=2, alpha=0.8)
            ax.annotate('PROFITABILITY BREACH', xy=(cross_week, 0), xytext=(cross_week+10, 50),
                        arrowprops=dict(facecolor='#d62728', edgecolor='#d62728', width=2, headwidth=8),
                        color='#d62728', weight='bold')
    elif metric == 'providers':
        ax.annotate('LATENT CAPACITY DEGRADATION', xy=(40, s['median'].min()), xytext=(20, s['median'].max()*0.6),
                    arrowprops=dict(facecolor='#ff7f0e', edgecolor='#ff7f0e', arrowstyle='wedge,tail_width=0.8', alpha=0.8),
                    color='#ff7f0e', weight='bold')
    
    ax.set_title(title)
    ax.set_xlabel('Week')
    ax.set_ylabel(ylab)
    ax.legend()
fig.suptitle('SCENARIO D: PROVIDER COST INFLATION (Profitability-Induced Churn)', weight='bold')
fig.tight_layout()
fig.savefig(FIGS / 'fig_cost_inflation_ono_profit_providers.png', dpi=220, bbox_inches='tight')
plt.close(fig)

# 7 Final retention across profiles
pivot_ret = final.pivot_table(index='profile_name', columns='scenario_label', values='retention_final')
pivot_ret = pivot_ret[[c for c in ['Baseline Neutral', 'Demand Contraction', 'Liquidity Shock', 'Competitive Yield Pressure', 'Provider Cost Inflation'] if c in pivot_ret.columns]]
fig, ax = plt.subplots(figsize=(13.6, 4.5))
pivot_ret.plot(kind='bar', ax=ax)
ax.annotate('HIGH VOLATILITY\nIN LIQUIDITY SHOCKS', xy=(4.05, pivot_ret.loc['ONOCOY', 'Liquidity Shock']), xytext=(3.8, 0.02),
            arrowprops=dict(facecolor='#2ca02c', edgecolor='#2ca02c', width=2, headwidth=8),
            color='#2ca02c', weight='bold', ha='right', va='center')
ax.set_title('Final Retention by Profile and Scenario')
ax.set_xlabel('Profile')
ax.set_ylabel('Retention (final / initial)')
ax.set_ylim(0, pivot_ret.max().max() * 1.35)
ax.legend(title='Scenario', loc='upper center', ncol=3)
fig.tight_layout()
fig.savefig(FIGS / 'fig_cross_scenario_retention_profiles.png', dpi=220, bbox_inches='tight')
plt.close(fig)

# 8 Final solvency across profiles
pivot_sol = final.pivot_table(index='profile_name', columns='scenario_label', values='solvency_final')
pivot_sol = pivot_sol[[c for c in ['Baseline Neutral', 'Demand Contraction', 'Liquidity Shock', 'Competitive Yield Pressure', 'Provider Cost Inflation'] if c in pivot_sol.columns]]
fig, ax = plt.subplots(figsize=(13.6, 4.5))
pivot_sol.plot(kind='bar', ax=ax)
ax.annotate('UNBOUNDED PROXY BLOWOUT\n(Helium / Grass)', xy=(2.0, pivot_sol.loc['Helium', 'Liquidity Shock']), xytext=(1.8, 140),
            arrowprops=dict(facecolor='#2ca02c', edgecolor='#2ca02c', width=2, headwidth=8),
            color='#2ca02c', weight='bold', ha='right', va='top')
ax.annotate('PROXY REMAINS BOUNDED\n(ONO)', xy=(4.05, 5), xytext=(4.05, 70),
            arrowprops=dict(facecolor='#1f77b4', edgecolor='#1f77b4', arrowstyle='wedge,tail_width=0.6', alpha=0.8),
            color='#1f77b4', weight='bold', ha='center')
ax.set_title('Final Incentive-Solvency Proxy by Profile and Scenario')
ax.set_xlabel('Profile')
ax.set_ylabel('Final Solvency Proxy')
ax.set_ylim(0, pivot_sol.max().max() * 1.35)
ax.legend(title='Scenario', loc='upper center', ncol=3)
fig.tight_layout()
fig.savefig(FIGS / 'fig_cross_scenario_solvency_profiles.png', dpi=220, bbox_inches='tight')
plt.close(fig)

# 9 ONO final delta heatmap vs baseline
ono = final[final['profile_id'] == ONO].copy()
base = ono[ono['scenario_id'] == 'baseline_neutral'].iloc[0]
metrics = ['retention_final', 'solvency_final', 'profit_final', 'utilisation_final', 'burn_to_mint_final']
scenario_ids = ['demand_contraction', 'liquidity_shock', 'competitive_yield_pressure', 'provider_cost_inflation']
rows = []
for sid in scenario_ids:
    row = ono[ono['scenario_id'] == sid].iloc[0]
    rows.append([((row[m] - base[m]) / (abs(base[m]) if abs(base[m]) > 1e-9 else 1.0)) for m in metrics])
arr = np.array(rows)
fig, ax = plt.subplots(figsize=(9.6, 4.5))
im = ax.imshow(arr, cmap='RdBu_r', aspect='auto', vmin=-1, vmax=1)
ax.set_xticks(np.arange(len(metrics)))
ax.set_xticklabels(['Retention', 'Solvency', 'Profit', 'Utilisation', 'Burn/Mint'])
ax.set_yticks(np.arange(len(scenario_ids)))
ax.set_yticklabels(['Demand contraction', 'Liquidity shock', 'Competitive yield', 'Cost inflation'])
ax.set_title('ONO: Final-Metric Delta vs Baseline (relative)')
for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        ax.text(j, i, f"{arr[i,j]:+.2f}", ha='center', va='center', color='black', fontsize=9.5)
fig.colorbar(im, ax=ax, shrink=0.85, label='Relative delta vs baseline')
fig.tight_layout()
fig.savefig(FIGS / 'fig_cross_scenario_ono_metric_deltas_heatmap.png', dpi=220, bbox_inches='tight')
plt.close(fig)

# 10 Signal timing chart
sig = signals.copy()
sig = sig.set_index('scenario_id')[[
    'earliest_price_signal_week',
    'earliest_utilisation_signal_week',
    'earliest_profit_signal_week',
    'lagged_provider_signal_week',
    'lagged_churn_signal_week',
]].reset_index()
labels = {
    'demand_contraction': 'Demand contraction',
    'liquidity_shock': 'Liquidity shock',
    'competitive_yield_pressure': 'Competitive yield',
    'provider_cost_inflation': 'Cost inflation',
}
fig, ax = plt.subplots(figsize=(12.6, 4.5))
x = np.arange(len(sig))
width = 0.16
cols = [
    ('earliest_price_signal_week', 'Price'),
    ('earliest_utilisation_signal_week', 'Utilisation'),
    ('earliest_profit_signal_week', 'Profit'),
    ('lagged_provider_signal_week', 'Providers'),
    ('lagged_churn_signal_week', 'Churn'),
]
for i, (col, name) in enumerate(cols):
    ax.bar(x + (i - 2) * width, sig[col], width=width, label=name)
ax.set_xticks(x)
ax.set_xticklabels([labels.get(v, v) for v in sig['scenario_id']], rotation=0)
ax.set_ylabel('First signal week')
ax.set_title('ONO: Signal-Timing by Stress Channel')
ax.legend(ncol=3)
fig.tight_layout()
fig.savefig(FIGS / 'fig_cross_scenario_signal_timing_ono.png', dpi=220, bbox_inches='tight')
plt.close(fig)

# Derived synthesis table for LaTeX alignment
# mechanism sensitivity proxy = std dev of final retention across profiles per scenario
sens = final.groupby('scenario_id')['retention_final'].std().to_dict()
def sens_band(v):
    if pd.isna(v):
        return 'Low'
    if v >= 0.010:
        return 'High'
    if v >= 0.0015:
        return 'Medium'
    return 'Low'

synth_rows = []
for _, row in signals.iterrows():
    sid = row['scenario_id']
    if sid == 'demand_contraction':
        earliest = f"utilisation (w{int(row['earliest_utilisation_signal_week'])})"
        lagging = f"providers/churn (w{int(row['lagged_provider_signal_week'])}/w{int(row['lagged_churn_signal_week'])})"
        signature = 'Reward--Demand Decoupling'
    elif sid == 'liquidity_shock':
        earliest = f"price (w{int(row['earliest_price_signal_week'])})"
        lagging = f"profit/churn (w{int(row['earliest_profit_signal_week'])}/w{int(row['lagged_churn_signal_week'])})"
        signature = 'Liquidity-Driven Compression'
    elif sid == 'competitive_yield_pressure':
        earliest = f"churn (w{int(row['lagged_churn_signal_week'])})"
        lagging = f"providers (w{int(row['lagged_provider_signal_week'])})"
        signature = 'Elastic Provider Exit'
    else:
        earliest = f"profit (w{int(row['earliest_profit_signal_week'])})"
        lagging = f"providers/churn (w{int(row['lagged_provider_signal_week'])}/w{int(row['lagged_churn_signal_week'])})"
        signature = 'Profitability-Induced Churn + Latent Capacity Degradation'
    synth_rows.append({
        'scenario_id': sid,
        'earliest_signal_observed': earliest,
        'lagging_signal_observed': lagging,
        'failure_signature': signature,
        'mechanism_sensitivity_band': sens_band(sens.get(sid, np.nan)),
    })

pd.DataFrame(synth_rows).to_csv(TABLES / 'dtse_cross_scenario_synthesis.csv', index=False)

print('Generated figures:', len(list(FIGS.glob('*.png'))))
print('Generated synthesis table:', TABLES / 'dtse_cross_scenario_synthesis.csv')
