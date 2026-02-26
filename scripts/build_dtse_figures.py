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
    ax.plot(df['week'], df['median'], label=label, color=color, linewidth=2)
    ax.fill_between(df['week'], df['p25'], df['p75'], color=color, alpha=0.2)


plt.rcParams.update({'figure.figsize': (10, 4.8), 'axes.grid': True, 'grid.alpha': 0.25})

# 1 Baseline price/providers
fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))
plot_line_with_band(axes[0], series_df(ONO, 'baseline_neutral', 'price'), 'Median (IQR)', '#1f77b4')
axes[0].set_title('Baseline (ONO): Price Signal')
axes[0].set_xlabel('Week')
axes[0].set_ylabel('Modeled Price (USD)')
axes[0].legend()
plot_line_with_band(axes[1], series_df(ONO, 'baseline_neutral', 'providers'), 'Median (IQR)', '#ff7f0e')
axes[1].set_title('Baseline (ONO): Active Providers')
axes[1].set_xlabel('Week')
axes[1].set_ylabel('Providers')
axes[1].legend()
fig.tight_layout()
fig.savefig(FIGS / 'fig_baseline_ono_price_providers.png', dpi=180)
plt.close(fig)

# 2 Baseline burn vs mint
fig, ax = plt.subplots(figsize=(10, 4.5))
plot_line_with_band(ax, series_df(ONO, 'baseline_neutral', 'minted'), 'Minted', '#d62728')
plot_line_with_band(ax, series_df(ONO, 'baseline_neutral', 'burned'), 'Burned', '#2ca02c')
ax.set_title('Baseline (ONO): Emissions vs Sinks')
ax.set_xlabel('Week')
ax.set_ylabel('Tokens / week')
ax.legend()
fig.tight_layout()
fig.savefig(FIGS / 'fig_baseline_ono_burn_mint.png', dpi=180)
plt.close(fig)

# 3 Demand contraction vs baseline (utilisation, burn, profit)
fig, axes = plt.subplots(1, 3, figsize=(15, 4.2))
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
        axes[i].legend()
fig.suptitle('ONO: Demand Contraction Deviations from Baseline')
fig.tight_layout()
fig.savefig(FIGS / 'fig_demand_contraction_ono_core.png', dpi=180)
plt.close(fig)

# 4 Liquidity shock price/churn
fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))
for ax, metric, title, ylab, color in [
    (axes[0], 'price', 'Price Signal', 'USD', '#9467bd'),
    (axes[1], 'churnCount', 'Churn Count', 'Providers/week', '#8c564b'),
]:
    b = series_df(ONO, 'baseline_neutral', metric)
    s = series_df(ONO, 'liquidity_shock', metric)
    ax.plot(b['week'], b['median'], label='Baseline', color='#1f77b4', linewidth=2)
    ax.plot(s['week'], s['median'], label='Liquidity shock', color=color, linewidth=2)
    ax.axvline(20, color='black', linestyle='--', alpha=0.4)
    ax.set_title(title)
    ax.set_xlabel('Week')
    ax.set_ylabel(ylab)
    ax.legend()
fig.suptitle('ONO: Liquidity Shock Transmission (event week=20)')
fig.tight_layout()
fig.savefig(FIGS / 'fig_liquidity_shock_ono_price_churn.png', dpi=180)
plt.close(fig)

# 5 Competitive yield pressure
fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))
for ax, metric, title, ylab, color in [
    (axes[0], 'providers', 'Active Providers', 'Providers', '#ff7f0e'),
    (axes[1], 'churnCount', 'Churn', 'Providers/week', '#d62728'),
]:
    b = series_df(ONO, 'baseline_neutral', metric)
    s = series_df(ONO, 'competitive_yield_pressure', metric)
    ax.plot(b['week'], b['median'], label='Baseline', color='#1f77b4', linewidth=2)
    ax.plot(s['week'], s['median'], label='Competitive yield', color=color, linewidth=2)
    ax.set_title(title)
    ax.set_xlabel('Week')
    ax.set_ylabel(ylab)
    ax.legend()
fig.suptitle('ONO: Competitive Yield Pressure Response')
fig.tight_layout()
fig.savefig(FIGS / 'fig_competitive_yield_ono_retention_churn.png', dpi=180)
plt.close(fig)

# 6 Cost inflation profit/providers
fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))
for ax, metric, title, ylab, color in [
    (axes[0], 'profit', 'Provider Profit', 'USD/week', '#d62728'),
    (axes[1], 'providers', 'Active Providers', 'Providers', '#ff7f0e'),
]:
    b = series_df(ONO, 'baseline_neutral', metric)
    s = series_df(ONO, 'provider_cost_inflation', metric)
    ax.plot(b['week'], b['median'], label='Baseline', color='#1f77b4', linewidth=2)
    ax.plot(s['week'], s['median'], label='Cost inflation', color=color, linewidth=2)
    ax.set_title(title)
    ax.set_xlabel('Week')
    ax.set_ylabel(ylab)
    ax.legend()
fig.suptitle('ONO: Provider Cost Inflation Response')
fig.tight_layout()
fig.savefig(FIGS / 'fig_cost_inflation_ono_profit_providers.png', dpi=180)
plt.close(fig)

# 7 Final retention across profiles
pivot_ret = final.pivot_table(index='profile_name', columns='scenario_label', values='retention_final')
pivot_ret = pivot_ret[[c for c in ['Baseline Neutral', 'Demand Contraction', 'Liquidity Shock', 'Competitive Yield Pressure', 'Provider Cost Inflation'] if c in pivot_ret.columns]]
fig, ax = plt.subplots(figsize=(12, 5))
pivot_ret.plot(kind='bar', ax=ax)
ax.set_title('Final Retention by Profile and Scenario')
ax.set_xlabel('Profile')
ax.set_ylabel('Retention (final / initial)')
ax.legend(title='Scenario', fontsize=8)
fig.tight_layout()
fig.savefig(FIGS / 'fig_cross_scenario_retention_profiles.png', dpi=180)
plt.close(fig)

# 8 Final solvency across profiles
pivot_sol = final.pivot_table(index='profile_name', columns='scenario_label', values='solvency_final')
pivot_sol = pivot_sol[[c for c in ['Baseline Neutral', 'Demand Contraction', 'Liquidity Shock', 'Competitive Yield Pressure', 'Provider Cost Inflation'] if c in pivot_sol.columns]]
fig, ax = plt.subplots(figsize=(12, 5))
pivot_sol.plot(kind='bar', ax=ax)
ax.set_title('Final Incentive-Solvency Proxy by Profile and Scenario')
ax.set_xlabel('Profile')
ax.set_ylabel('Final Solvency Proxy')
ax.legend(title='Scenario', fontsize=8)
fig.tight_layout()
fig.savefig(FIGS / 'fig_cross_scenario_solvency_profiles.png', dpi=180)
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
fig, ax = plt.subplots(figsize=(8.5, 4.8))
im = ax.imshow(arr, cmap='RdBu_r', aspect='auto', vmin=-1, vmax=1)
ax.set_xticks(np.arange(len(metrics)))
ax.set_xticklabels(['Retention', 'Solvency', 'Profit', 'Utilisation', 'Burn/Mint'])
ax.set_yticks(np.arange(len(scenario_ids)))
ax.set_yticklabels(['Demand contraction', 'Liquidity shock', 'Competitive yield', 'Cost inflation'])
ax.set_title('ONO: Final-Metric Delta vs Baseline (relative)')
for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        ax.text(j, i, f"{arr[i,j]:+.2f}", ha='center', va='center', color='black', fontsize=8)
fig.colorbar(im, ax=ax, shrink=0.8, label='Relative delta vs baseline')
fig.tight_layout()
fig.savefig(FIGS / 'fig_cross_scenario_ono_metric_deltas_heatmap.png', dpi=180)
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
fig, ax = plt.subplots(figsize=(11, 4.8))
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
ax.legend(ncol=3, fontsize=8)
fig.tight_layout()
fig.savefig(FIGS / 'fig_cross_scenario_signal_timing_ono.png', dpi=180)
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
