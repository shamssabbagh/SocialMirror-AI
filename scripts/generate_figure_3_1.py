#!/usr/bin/env python3
"""
SocialMirror-AI: Generation script for Figure 3.1
Illustrative Synthetic Simulation Scenario: State Vector Dynamics Across Interventions
Course: AI Agents & Vibe Coding, University of Haifa
Authors: Shams Sabbagh & Malak Farouja
"""

import os
import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def run_simulation(config_path):
    with open(config_path, 'r', encoding='utf-8') as f:
        config = json.load(f)

    params = config["parameters"]
    steps = params["steps"]
    t = np.arange(1, steps + 1)

    # 1. Deterministic Stimuli Generation
    np.random.seed(42)
    s_comp_base = np.array([
        0.35, 0.40, 0.48, 0.55, 0.62, 0.74, 0.82, 0.88, 0.85, 0.81,
        0.79, 0.83, 0.78, 0.72, 0.75, 0.80, 0.85, 0.87, 0.82, 0.80,
        0.76, 0.74, 0.79, 0.81, 0.83, 0.85, 0.82, 0.78, 0.75, 0.71
    ])
    e_inf_base = np.array([
        0.30, 0.35, 0.42, 0.50, 0.60, 0.70, 0.78, 0.82, 0.80, 0.76,
        0.75, 0.81, 0.74, 0.68, 0.72, 0.77, 0.83, 0.85, 0.80, 0.78,
        0.72, 0.70, 0.75, 0.78, 0.80, 0.82, 0.79, 0.74, 0.70, 0.68
    ])

    # 2. State Trajectories across 3 Conditions
    init_se = params["initial_state"]["self_esteem"]
    rate_erosion = params["coefficients"]["contrast_erosion_rate"]
    rate_recovery = params["coefficients"]["cognitive_reframing_recovery"]

    # Condition A: Baseline Unmitigated Feed
    se_baseline = np.zeros(steps)
    curr_se = init_se
    for i in range(steps):
        # contrast erosion proportional to comparison salience
        erosion = rate_erosion * (s_comp_base[i] - 0.35)
        curr_se = max(0.32, curr_se - erosion + 0.005 * (0.72 - curr_se))
        se_baseline[i] = curr_se

    # Condition B: Rigid Commercial Screen-Time Blocker (Cutoff at t=18)
    cutoff_step = params["intervention_thresholds"]["screentime_cutoff_step"]
    se_screentime = np.zeros(steps)
    curr_se = init_se
    for i in range(steps):
        if i < cutoff_step:
            erosion = rate_erosion * (s_comp_base[i] - 0.35)
            curr_se = max(0.32, curr_se - erosion + 0.005 * (0.72 - curr_se))
            se_screentime[i] = curr_se
        else:
            # Abrupt cutoff: freezing damage with mild post-reactance stagnation
            curr_se += 0.004 * (0.72 - curr_se)
            se_screentime[i] = curr_se

    # Condition C: SocialMirror-AI Autonomy-Supportive Cognitive Mirror
    intervention_step = params["intervention_thresholds"]["intervention_step"]
    se_socialmirror = np.zeros(steps)
    curr_se = init_se
    for i in range(steps):
        if i < intervention_step:
            erosion = rate_erosion * (s_comp_base[i] - 0.35)
            curr_se = max(0.32, curr_se - erosion + 0.005 * (0.72 - curr_se))
            se_socialmirror[i] = curr_se
        else:
            # Reflection prompt reframes perception: downward assimilation & resilience
            reframing_boost = rate_recovery * (1.0 - (s_comp_base[i] * 0.4))
            curr_se = min(0.74, curr_se + reframing_boost)
            se_socialmirror[i] = curr_se

    return t, s_comp_base, e_inf_base, se_baseline, se_screentime, se_socialmirror, config

def create_plot(t, s_comp, e_inf, se_base, se_st, se_sm, config, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    # Style configuration
    plt.rcParams['font.sans-serif'] = 'Arial'
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['axes.edgecolor'] = '#64748B'
    plt.rcParams['axes.linewidth'] = 0.9

    dark_purple = '#2E1A47'
    royal_purple = '#5E35B1'
    lavender_border = '#7E57C2'
    lavender_bg = '#F8FAFC'
    alert_rose = '#E11D48'
    slate_gray = '#64748B'
    emerald_green = '#059669'

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9.5, 6.2), dpi=300, sharex=True,
                                   gridspec_kw={'height_ratios': [1, 1.4]})
    fig.patch.set_facecolor('#FFFFFF')
    ax1.set_facecolor(lavender_bg)
    ax2.set_facecolor(lavender_bg)

    # ------------------ TOP PANEL: Input Stimuli ------------------
    ax1.plot(t, s_comp, color=dark_purple, linewidth=2.0, label=r'Upward Comparison Salience ($\mathcal{S}_{\mathrm{comp}}$)')
    ax1.plot(t, e_inf, color=lavender_border, linewidth=1.8, linestyle='--', label=r'Influencer Exposure Index ($\mathcal{E}_{\mathrm{inf}}$)')

    # Threshold line
    theta = 0.65
    ax1.axhline(theta, color=alert_rose, linestyle=':', linewidth=1.2, alpha=0.85,
                label=r'Intervention Threshold ($\theta_{\mathrm{comp}} = 0.65$)')

    # Trigger marker
    ax1.scatter([12], [s_comp[11]], color=royal_purple, s=65, zorder=5)
    ax1.annotate('Threshold Exceeded\n(Trigger Step 12)', xy=(12, s_comp[11]), xytext=(13.2, 0.92),
                 fontsize=8.5, fontweight='bold', color=royal_purple,
                 arrowprops=dict(arrowstyle='->', color=royal_purple, lw=1.1))

    ax1.set_ylabel('Stimulus Intensity\n[0.0 - 1.0]', fontsize=9, fontweight='bold', color=dark_purple)
    ax1.set_ylim(0.2, 1.05)
    ax1.grid(True, linestyle='--', alpha=0.45, color='#CBD5E1')
    ax1.legend(loc='lower left', fontsize=8, framealpha=0.92, facecolor='#FFFFFF', edgecolor='#CBD5E1')
    ax1.set_title('Figure 3.1: Synthetic Simulation Scenario — State Vector Dynamics Across Interventions\n'
                  '(Illustrative Prototype Model: Stimuli Exposure vs. Momentary Self-Esteem Trajectories)',
                  fontsize=10.5, fontweight='bold', color=dark_purple, pad=10)

    # ------------------ BOTTOM PANEL: State Vector Dynamics ------------------
    # Baseline
    ax2.plot(t, se_base, color=alert_rose, linewidth=2.0, linestyle=':',
             label='Condition A: Unmitigated Algorithmic Feed (No Intervention)')

    # Commercial Screen Time
    ax2.plot(t, se_st, color=slate_gray, linewidth=2.0, linestyle='--',
             label='Condition B: Commercial Screen-Time Blocker (Forced Lockout at Step 18)')

    # SocialMirror-AI
    ax2.plot(t, se_sm, color=royal_purple, linewidth=2.4, linestyle='-',
             label='Condition C: SocialMirror-AI Cognitive Mirror (Reflection Prompt at Step 12)')

    # Highlight reflection scaffold zone
    ax2.axvspan(12, 18, color='#EDE7F6', alpha=0.6, label='Scaffold Active Window (Metacognitive Reframing)')

    # Lockout point in Screen-Time
    ax2.scatter([18], [se_st[17]], color=slate_gray, s=55, zorder=5)
    ax2.annotate('Rigid Screen Lock\n(Reactance Spike)', xy=(18, se_st[17]), xytext=(18.8, 0.40),
                 fontsize=8.5, fontweight='bold', color=slate_gray,
                 arrowprops=dict(arrowstyle='->', color=slate_gray, lw=1.1))

    # Recovery annotation
    ax2.annotate('Cognitive Reframing Recovery\n(Downward Assimilation, $w_t^{\\mathrm{SE}} \\to 0.72$)',
                 xy=(21, se_sm[20]), xytext=(15.2, 0.79),
                 fontsize=8.5, fontweight='bold', color=royal_purple,
                 arrowprops=dict(arrowstyle='->', color=royal_purple, lw=1.2))

    ax2.set_xlabel('Simulation Step / Discrete Post Exposure Event ($t$)', fontsize=9.5, fontweight='bold', color=dark_purple)
    ax2.set_ylabel(r'Momentary Self-Esteem ($w_t^{\mathrm{SE}}$)' + '\n[Normalized State 0.0 - 1.0]',
                   fontsize=9, fontweight='bold', color=dark_purple)
    ax2.set_ylim(0.30, 0.88)
    ax2.set_xlim(1, 30)
    ax2.xaxis.set_major_locator(ticker.MultipleLocator(2))
    ax2.grid(True, linestyle='--', alpha=0.45, color='#CBD5E1')
    ax2.legend(loc='lower left', fontsize=8, framealpha=0.92, facecolor='#FFFFFF', edgecolor='#CBD5E1')

    # Watermark / Note indicating synthetic nature
    ax2.text(0.985, 0.04, 'Synthetic Simulation Scenario (Conceptual Illustrative Prototype)',
             transform=ax2.transAxes, fontsize=8, fontstyle='italic', color='#94A3B8',
             ha='right', va='bottom', bbox=dict(boxstyle='square,pad=0.2', facecolor='#FFFFFF', edgecolor='none', alpha=0.8))

    plt.tight_layout()

    pdf_path = os.path.join(output_dir, "figure_3_1_simulation.pdf")
    png_path = os.path.join(output_dir, "figure_3_1_simulation.png")

    fig.savefig(pdf_path, format='pdf', bbox_inches='tight')
    fig.savefig(png_path, format='png', dpi=300, bbox_inches='tight')
    plt.close(fig)

    print(f"Generated successfully:\n  {pdf_path}\n  {png_path}")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_file = os.path.join(script_dir, "simulation_parameters.json")
    repo_root = os.path.dirname(script_dir)
    assets_dir = os.path.join(repo_root, "report", "assets")

    t, s_comp, e_inf, se_base, se_st, se_sm, config = run_simulation(config_file)
    create_plot(t, s_comp, e_inf, se_base, se_st, se_sm, config, assets_dir)
