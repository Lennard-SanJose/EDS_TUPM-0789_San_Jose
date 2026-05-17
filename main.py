import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os

class SanJoseEngineeringPipeline:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None
        if not os.path.exists('outputs'): os.makedirs('outputs')

    def ingest_and_clean(self):
        print("Ingesting HVA-04 Dataset...")
        self.df = pd.read_csv(self.file_path, usecols=['breath_id', 'u_in', 'pressure', 'time_step'])
        # Filtering for your unique range
        self.df = self.df[(self.df['breath_id'] >= 1900) & (self.df['breath_id'] <= 2100)].copy()
        self.df.to_csv('data/dataset_cleaned.csv', index=False)
        print("✅ Static data cleaned and saved to data/ folder.")

    def calculate_analytics(self):
        print("\n--- ENGINEERING DATA ANALYTICS ---")
        try:
            if self.df is not None and not self.df.empty:
                target_col = 'u_in'
                data_array = self.df[target_col].to_numpy()

                # NumPy Matrix Calculations
                mean_val = np.mean(data_array)
                median_val = np.median(data_array)
                variance_val = np.var(data_array)
                std_val = np.std(data_array)
                
                # New Metrics Calculations
                skew_val = pd.Series(data_array).skew()
                
                q1 = np.percentile(data_array, 25)
                q3 = np.percentile(data_array, 75)
                iqr = q3 - q1
                lower_bound = q1 - 1.5 * iqr
                upper_bound = q3 + 1.5 * iqr
                outliers_count = np.sum((data_array < lower_bound) | (data_array > upper_bound))
                
                numeric_df = self.df.select_dtypes(include=[np.number])
                correlation_matrix = numeric_df.corr()

                # Printing Existing & New Metrics
                print(f"Target Column Evaluated: {target_col}")
                print(f"Mean: {mean_val:.4f}")
                print(f"Median: {median_val:.4f}")
                print(f"Variance: {variance_val:.4f}")
                print(f"Standard Deviation: {std_val:.4f}")
                print(f"Skewness: {skew_val:.4f}")
                print(f"Outliers Detected: {outliers_count} data points")
                
                print("\n🔗 --- CORRELATION MATRIX ---")
                print(correlation_matrix)
            else:
                print("[ERROR] Cleaned dataframe is empty.")
                
        except Exception as e:
            print(f"[ERROR] Analytical calculation failed: {e}")
        print("----------------------------------------\n")

    def generate_static_graphs(self):
        """Generates the 3 required static plots"""
        print("Generating Static Graphs...")
        
        # 1. Histogram (Distribution)
        plt.figure(figsize=(8, 5))
        plt.hist(self.df['u_in'], bins=30, color='purple', edgecolor='white')
        plt.title('Static Graph 1: Flow Rate Distribution')
        plt.savefig('outputs/histogram_flow.png')
        
        # 2. Boxplot (Outliers/Spread)
        plt.figure(figsize=(8, 5))
        plt.boxplot(self.df['u_in'])
        plt.title('Static Graph 2: Flow Rate Spread (Boxplot)')
        plt.savefig('outputs/boxplot_flow.png')
        
        # 3. Scatter Plot (Flow vs Pressure)
        plt.figure(figsize=(8, 5))
        plt.scatter(self.df['u_in'], self.df['pressure'], alpha=0.5, color='teal')
        plt.title('Static Graph 3: Flow vs Pressure Correlation')
        plt.savefig('outputs/scatter_correlation.png')
        plt.close('all')
        print("✅ 3 Static graphs saved to outputs/ folder.")

    def generate_animations(self):
        """Generates the 2 required animated graphs"""
        print("Generating Animations (this may take a minute)...")
        
        # Animation 1: Flow Trend over Time
        fig, ax = plt.subplots()
        sample_breath = self.df[self.df['breath_id'] == 1900]
        line, = ax.plot([], [], color='red')
        ax.set_xlim(0, sample_breath['time_step'].max())
        ax.set_ylim(0, sample_breath['u_in'].max() + 5)
        
        def update(i):
            line.set_data(sample_breath['time_step'][:i], sample_breath['u_in'][:i])
            return line,

        ani = animation.FuncAnimation(fig, update, frames=len(sample_breath), interval=50)
        ani.save('outputs/animation_flow_trend.gif', writer='pillow')
        
        # Animation 2: Pressure Build-up
        fig2, ax2 = plt.subplots()
        line2, = ax2.plot([], [], color='blue')
        ax2.set_xlim(0, sample_breath['time_step'].max())
        ax2.set_ylim(0, sample_breath['pressure'].max() + 5)

        def update2(i):
            line2.set_data(sample_breath['time_step'][:i], sample_breath['pressure'][:i])
            return line2,

        ani2 = animation.FuncAnimation(fig2, update2, frames=len(sample_breath), interval=50)
        ani2.save('outputs/animation_pressure_trend.gif', writer='pillow')
        print("✅ 2 Animations saved to outputs/ folder.")

if __name__ == "__main__":
    pipeline = SanJoseEngineeringPipeline('data/dataset_original.csv')
    pipeline.ingest_and_clean()
    
    # Call the new calculation function here
    pipeline.calculate_analytics()
    
    pipeline.generate_static_graphs()
    pipeline.generate_animations()