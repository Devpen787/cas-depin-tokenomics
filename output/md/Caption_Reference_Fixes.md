# Caption and Reference Fixes (No Edits Applied)

Per `CAS_FORMATTING_AND_STYLE.md`, every figure/table should be referenced in the text. The items below add minimal in-text references for labeled tables that currently have captions/labels but no `\ref{...}` / `\autoref{...}` usage anywhere in the thesis source.

## CR-001 (Reference Onocoy case summary table)
- **File:** `sections/personA_onocoy.tex`
- **Location:** Line 22 (immediately before `\\begin{table}[ht]`)
- **Current:**
```tex
\subsection{Case-at-a-Glance Summary}
\begin{table}[ht]
```
- **Proposed:**
```tex
\subsection{Case-at-a-Glance Summary}
Table~\ref{tab:onocoy_case_at_a_glance} provides a compact descriptive summary of the Onocoy empirical case used as the thesis anchor.
\begin{table}[ht]
```
- **Rationale:** `tab:onocoy_case_at_a_glance` is labeled but not referenced in the body text.
- **Approved:** YES

## CR-002 (Reference scenario interpretation summary table)
- **File:** `sections/personC_results.tex`
- **Location:** Line 62 (immediately after `\\paragraph*{Scenario Interpretation Summary}`)
- **Current:**
```tex
\paragraph*{Scenario Interpretation Summary}
\begin{table}[ht]
```
- **Proposed:**
```tex
\paragraph*{Scenario Interpretation Summary}
Table~\ref{tab:dtse_scenario_interpretation_cards} summarizes scenario inputs, first-signal metric families, and DTSE-conditional interpretation rules used in this section.
\begin{table}[ht]
```
- **Rationale:** `tab:dtse_scenario_interpretation_cards` is labeled but not referenced in the text.
- **Approved:** YES

## CR-003 (Reference metric applicability matrix)
- **File:** `sections/empirical_analysis.tex`
- **Location:** Line 112 (immediately before the table beginning at line 114)
- **Current:**
```tex
\noindent\textbf{Comparative inference rule:} a metric marked \emph{N/R} for a given project-window is excluded from comparative ranking in this empirical chapter. It may still appear as context, but it is not used as evidence for cross-project ordering.

\begin{table}[ht]
```
- **Proposed:**
```tex
\noindent\textbf{Comparative inference rule:} a metric marked \emph{N/R} for a given project-window is excluded from comparative ranking in this empirical chapter. It may still appear as context, but it is not used as evidence for cross-project ordering.

Table~\ref{tab:metric_applicability_matrix} summarizes applicability status for the empirical sample and highlights primary constraints by project.
\begin{table}[ht]
```
- **Rationale:** `tab:metric_applicability_matrix` is labeled but not referenced anywhere in the thesis text.
- **Approved:** YES

## CR-004 (Reference historical stress windows summary table)
- **File:** `sections/empirical_analysis.tex`
- **Location:** Line 204 (immediately after `\\paragraph*{Historical Stress Windows at a Glance}`)
- **Current:**
```tex
\paragraph*{Historical Stress Windows at a Glance}
\begin{table}[ht]
```
- **Proposed:**
```tex
\paragraph*{Historical Stress Windows at a Glance}
Table~\ref{tab:empirical_stress_windows_summary} summarizes the event windows used to motivate the DTSE scenario channels and their intended mapping.
\begin{table}[ht]
```
- **Rationale:** `tab:empirical_stress_windows_summary` is labeled but not referenced in the text.
- **Approved:** YES

## CR-005 (Reference override ledger table in appendix)
- **File:** `sections/appendix.tex`
- **Location:** Line 169 (first paragraph of Appendix Section `app:dtse_override_ledger`)
- **Current:**
```tex
This table documents profile-specific overrides and global heterogeneity rules used in the DTSE runs reported in Chapter~\ref{sec:simulation_results}. All entries listed here are modeled assumptions (including calibration choices) rather than empirical estimates of real-world protocol behavior. Each entry is traceable to exported configuration and registry artifacts referenced by the frozen run manifest. The table is provided for transparency and reproducibility and does not imply causal attribution or performance claims.
```
- **Proposed:**
```tex
Table~\ref{tab:app_dtse_override_ledger} documents profile-specific overrides and global heterogeneity rules used in the DTSE runs reported in Chapter~\ref{sec:simulation_results}. All entries listed here are modeled assumptions (including calibration choices) rather than empirical estimates of real-world protocol behavior. Each entry is traceable to exported configuration and registry artifacts referenced by the frozen run manifest. The table is provided for transparency and reproducibility and does not imply causal attribution or performance claims.
```
- **Rationale:** `tab:app_dtse_override_ledger` is labeled but not referenced in text anywhere (including within the appendix).
- **Approved:** YES

## CR-006 (Reference empirical metric applicability catalogue table in appendix)
- **File:** `sections/appendix.tex`
- **Location:** Line 251 (Appendix Section `app:empirical_metric_applicability`, immediately before the table beginning at line 253)
- **Current:**
```tex
This section documents the metric-applicability contract used in Chapter~\ref{sec:empirical_analysis}. It governs only empirical event-window interpretation and does not modify the pre-specified DTSE reporting set in Chapter~\ref{sec:simulation_results}.

\begin{table}[ht]
```
- **Proposed:**
```tex
This section documents the metric-applicability contract used in Chapter~\ref{sec:empirical_analysis}. It governs only empirical event-window interpretation and does not modify the pre-specified DTSE reporting set in Chapter~\ref{sec:simulation_results}.

Table~\ref{tab:app_empirical_metric_catalogue} records the empirical metric-applicability catalogue and its interpretive rules.
\begin{table}[ht]
```
- **Rationale:** `tab:app_empirical_metric_catalogue` is labeled but not referenced in text anywhere.
- **Approved:** YES

## CR-007 (Reference Onocoy metric applicability profile table in appendix)
- **File:** `sections/appendix.tex`
- **Location:** Line 272 (immediately before the table beginning at line 273)
- **Current:**
```tex
\end{table}

\begin{table}[ht]
```
- **Proposed:**
```tex
\end{table}

Table~\ref{tab:app_onocoy_metric_applicability} summarizes the Onocoy-specific applicability profile used for empirical interpretation in Chapter~\ref{sec:empirical_analysis}.
\begin{table}[ht]
```
- **Rationale:** `tab:app_onocoy_metric_applicability` is labeled but not referenced in text anywhere.
- **Approved:** YES

