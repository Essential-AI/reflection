import pandas as pd
import matplotlib.pyplot as plt
import os

def create_olmo_consolidated_plot(df, task, self_reflect=False):
    """Create separate plots for each metric showing all OLMo models for a specific task."""
    model_names = {
        "OLMo-2-1124-7B": "OLMo-2-7B",
        "OLMo-2-1124-13B": "OLMo-2-13B",
        "OLMo-2-0325-32B": "OLMo-2-32B",
    }

    markers = {
    7: {"color": "#1f77b4", "marker": "o"},  
    13: {"color": "#2ca02c", "marker": "^"}, 
    32: {"color": "#f5b800", "marker": "s"}, 
    }

    if self_reflect:
        task_df = df[df["Task_family"] == task]  
    else:
        task_df = df[df["Task"] == task]
    if task_df.empty:
        print(f"Warning: Task '{task}' not found in data")
        return None

    generated_plots = []

    metrics = task_df["Metric"].unique()
    for task_metric in metrics:
        plt.figure(figsize=(10, 6))
        for model, display_name in model_names.items():
            
            if self_reflect:
                model_df = df.loc[
                (df["Model"] == model)
                & (df["Task_family"] == task)
                & (df["Metric"] == task_metric)
            ].copy()
            else:
                model_df = df.loc[
                    (df["Model"] == model)
                    & (df["Task"] == task)
                    & (df["Metric"] == task_metric)
                ].copy()
                
            size = model_df["olmo-params"].iloc[0]
            style = markers[size]

            plt.scatter(
                model_df["Flops"],
                model_df["Average"],
                color=style["color"],
                marker=style["marker"],
                alpha=0.8,
                label=display_name,
            )
                    
        task_metric_label = task_metric.replace("_", " ")
        task_metric_label = task_metric_label.replace("impl", "implicit")
        task_metric_label = task_metric_label.replace("expl", "explicit")
        metric_suffix = (
            task_metric.replace(",", "_").replace("@", "_").replace("/", "_")
        )
        prefix = "self_reflect" if self_reflect else "situational"
        filename = f"{prefix}_olmo2_{task}_{metric_suffix}"
        plt.xlabel("Log Pre-Training Compute", fontsize=14)
        plt.ylabel(task_metric_label.title(), fontsize=14)
        # plt.title(filename, fontsize=14)
        plt.grid(False)
        plt.legend(fontsize=12)        
        plots_dir = "plots_self" if self_reflect else "plots_situational"
        plt.savefig(os.path.join(plots_dir, filename), bbox_inches="tight")
        plt.close()

        generated_plots.append(filename)

    print(f"Generated {len(generated_plots)} plots:")
    for plot in generated_plots:
        print(f"  {plot}")

def create_qwen_all_tasks_plot(df):
    """Create a single plot showing Qwen models for all tasks."""

    fig, ax = plt.subplots(figsize=(12, 8))

    colors = [
        "blue", "red", "green", "purple", "orange", "brown", "pink", "gray", "cyan",
        "magenta", "yellow", "lime", "navy", "maroon", "teal"
    ]

    handles = []
    labels = []

    tasks = df["Task"].unique()

    for task, color in zip(tasks, colors):
        model_df = df.loc[
                    df["Task"] == task
                ].copy()

        if not model_df.empty:
            model_df = model_df.sort_values("Size")
            scores = model_df["Average"]
            label = f"{task.replace('_', ' ')}"
            
            line = ax.plot(
                model_df["Flops"], scores, marker="o", color=color, label=label
            )
            if label == 'bbh adv':
                label = 'BBH'
            elif label == 'cruxeval i adv':
                label = 'cruxeval-i'
            elif label == 'cruxeval o adv':
                label = 'cruxeval-o'
            elif label == 'gsm8k adv':
                label = 'GSM8K'
            elif label == 'gsm8k-platinum adv':
                label = 'GSM8K-Platinum'
            else:
                label = 'TriviaQA'

            handles.append(line[0])
            labels.append(label)

    ax.set_xlabel("Log Pre-Training Compute", fontsize=14)
    ax.set_ylabel("Score", fontsize=14)  # Since we only have one metric per task, we can just use "Score"

    ax.legend(
        handles,
        labels,
        loc="upper left",
    )

    filename = "situational_qwen2.5_all_tasks.png"
    plt.savefig(os.path.join("plots_qwen", filename), bbox_inches="tight")
    plt.close()

    print(f"Generated {filename}")

def main():
    tasks = [
        "bbh_adv",
        "cruxeval_i_adv",
        "cruxeval_o_adv",
        "gsm8k_adv",
        "gsm8k-platinum_adv",
        "triviaqa_adv"
    ]
    # csvs and self_reflect boolean
    olmo_results = {'experiment_results_situational_reflection_250328_final_public.csv': False,
           'experiment_results_self_reflection_250328_final_public.csv': True}

    qwen_results = 'experiment_results_qwen_250328_final_public.csv'
    
    for result in olmo_results:
        df = pd.read_csv(result)
        for task in tasks:
            create_olmo_consolidated_plot(df, task, olmo_results[result])
    
    qwen_df = pd.read_csv(qwen_results)
    create_qwen_all_tasks_plot(qwen_df)
        

if __name__ == '__main__':
    main()
