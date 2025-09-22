import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import random
import webbrowser

class HealthSurveillanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("HealthPool Ecosystem For Water-Borne Diseases - AeroPace.")
        self.root.geometry("1000x700")
        self.root.configure(bg='#008080')
        
        # Style configuration
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Configure colors
        self.style.configure('TFrame', background='#f0f8ff')
        self.style.configure('TLabel', background='#f0f8ff', font=('Arial', 10))
        self.style.configure('Header.TLabel', background='#2c7da0', foreground='white', font=('Arial', 14, 'bold'))
        self.style.configure('TButton', font=('Arial', 10), background='#468faf')
        self.style.map('TButton', background=[('active', '#3a7c95')])
        self.style.configure('TNotebook', background='#f0f8ff')
        self.style.configure('TNotebook.Tab', font=('Arial', 10, 'bold'), padding=[10, 5])
        
        # Create notebook for tabs
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Create frames for each tab
        self.dashboard_frame = ttk.Frame(self.notebook)
        self.data_entry_frame = ttk.Frame(self.notebook)
        self.water_quality_frame = ttk.Frame(self.notebook)
        self.alerts_frame = ttk.Frame(self.notebook)
        
        self.notebook.add(self.dashboard_frame, text='Dashboard')
        self.notebook.add(self.data_entry_frame, text='Data Entry')
        self.notebook.add(self.water_quality_frame, text='Water Quality')
        self.notebook.add(self.alerts_frame, text='Alerts')
        
        # Initialize data
        self.symptoms_data = []
        self.water_quality_data = []
        self.alerts = []
        
        # Create all tabs
        self.create_dashboard_tab()
        self.create_data_entry_tab()
        self.create_water_quality_tab()
        self.create_alerts_tab()
        
        # Generate some sample data
        self.generate_sample_data()
        
    def create_dashboard_tab(self):
        # Header
        header_frame = ttk.Frame(self.dashboard_frame)
        header_frame.pack(fill='x', pady=10)
        
        header = ttk.Label(header_frame, text="Health Surveillance Dashboard", style='Header.TLabel')
        header.pack(fill='x', ipady=10)
        
        # Summary statistics frame
        stats_frame = ttk.LabelFrame(self.dashboard_frame, text="Summary Statistics")
        stats_frame.pack(fill='x', padx=10, pady=10)
        
        # Stats in a grid
        stats_grid = ttk.Frame(stats_frame)
        stats_grid.pack(fill='x', padx=10, pady=10)
        
        ttk.Label(stats_grid, text="Total Cases Reported:", font=('Arial', 10, 'bold')).grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.total_cases_label = ttk.Label(stats_grid, text="0", foreground="blue", font=('Arial', 10, 'bold'))
        self.total_cases_label.grid(row=0, column=1, sticky="w", padx=5, pady=5)
        
        ttk.Label(stats_grid, text="Active Alerts:", font=('Arial', 10, 'bold')).grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.active_alerts_label = ttk.Label(stats_grid, text="0", foreground="red", font=('Arial', 10, 'bold'))
        self.active_alerts_label.grid(row=1, column=1, sticky="w", padx=5, pady=5)
        
        ttk.Label(stats_grid, text="Water Sources Tested:", font=('Arial', 10, 'bold')).grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.water_tested_label = ttk.Label(stats_grid, text="0", foreground="green", font=('Arial', 10, 'bold'))
        self.water_tested_label.grid(row=2, column=1, sticky="w", padx=5, pady=5)
        
        ttk.Label(stats_grid, text="High Risk Areas:", font=('Arial', 10, 'bold')).grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.high_risk_label = ttk.Label(stats_grid, text="0", foreground="orange", font=('Arial', 10, 'bold'))
        self.high_risk_label.grid(row=3, column=1, sticky="w", padx=5, pady=5)
        
        # Recent alerts frame
        alerts_frame = ttk.LabelFrame(self.dashboard_frame, text="Recent Alerts")
        alerts_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        self.alerts_listbox = tk.Listbox(alerts_frame, height=8, font=('Arial', 10))
        self.alerts_listbox.pack(fill='both', expand=True, padx=5, pady=5)
        
    def create_data_entry_tab(self):
        # Header
        header_frame = ttk.Frame(self.data_entry_frame)
        header_frame.pack(fill='x', pady=10)
        
        header = ttk.Label(header_frame, text="Health Data Entry Form", style='Header.TLabel')
        header.pack(fill='x', ipady=10)
        
        # Main content frame
        content_frame = ttk.Frame(self.data_entry_frame)
        content_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Form frame
        form_frame = ttk.LabelFrame(content_frame, text="Patient Information")
        form_frame.pack(fill='both', side='left', expand=True, padx=5, pady=5)
        
        # Form fields
        ttk.Label(form_frame, text="Patient ID:", font=('Arial', 10, 'bold')).grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.patient_id = ttk.Entry(form_frame, font=('Arial', 10))
        self.patient_id.grid(row=0, column=1, padx=10, pady=5, sticky='ew')
        
        ttk.Label(form_frame, text="Age:", font=('Arial', 10, 'bold')).grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.age = ttk.Entry(form_frame, font=('Arial', 10))
        self.age.grid(row=1, column=1, padx=10, pady=5, sticky='ew')
        
        ttk.Label(form_frame, text="Location/Village:", font=('Arial', 10, 'bold')).grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.location = ttk.Entry(form_frame, font=('Arial', 10))
        self.location.grid(row=2, column=1, padx=10, pady=5, sticky='ew')
        
        ttk.Label(form_frame, text="Date:", font=('Arial', 10, 'bold')).grid(row=3, column=0, sticky="w", padx=10, pady=5)
        self.date = ttk.Entry(form_frame, font=('Arial', 10))
        self.date.insert(0, datetime.now().strftime("%Y-%m-%d"))
        self.date.grid(row=3, column=1, padx=10, pady=5, sticky='ew')
        
        # Symptoms frame
        symptoms_frame = ttk.LabelFrame(form_frame, text="Symptoms")
        symptoms_frame.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="we")
        
        self.fever = tk.BooleanVar()
        ttk.Checkbutton(symptoms_frame, text="Fever", variable=self.fever).grid(row=0, column=0, sticky="w", padx=10, pady=5)
        
        self.diarrhea = tk.BooleanVar()
        ttk.Checkbutton(symptoms_frame, text="Diarrhea", variable=self.diarrhea).grid(row=0, column=1, sticky="w", padx=10, pady=5)
        
        self.vomiting = tk.BooleanVar()
        ttk.Checkbutton(symptoms_frame, text="Vomiting", variable=self.vomiting).grid(row=1, column=0, sticky="w", padx=10, pady=5)
        
        self.dehydration = tk.BooleanVar()
        ttk.Checkbutton(symptoms_frame, text="Dehydration", variable=self.dehydration).grid(row=1, column=1, sticky="w", padx=10, pady=5)
        
        # Submit button
        ttk.Button(form_frame, text="Submit Data", command=self.submit_health_data).grid(row=5, column=0, columnspan=2, pady=10)
        
        # Recent entries frame
        entries_frame = ttk.LabelFrame(content_frame, text="Recent Entries")
        entries_frame.pack(fill='both', side='right', expand=True, padx=5, pady=5)
        
        # Create a text widget for entries
        self.entries_text = tk.Text(entries_frame, height=20, width=40, font=('Arial', 10))
        scrollbar = ttk.Scrollbar(entries_frame, orient='vertical', command=self.entries_text.yview)
        self.entries_text.configure(yscrollcommand=scrollbar.set)
        
        self.entries_text.pack(side='left', fill='both', expand=True, padx=5, pady=5)
        scrollbar.pack(side='right', fill='y')
        
        # Configure grid weights
        form_frame.columnconfigure(1, weight=1)
        
    def create_water_quality_tab(self):
        # Header
        header_frame = ttk.Frame(self.water_quality_frame)
        header_frame.pack(fill='x', pady=10)
        
        header = ttk.Label(header_frame, text="Water Quality Monitoring", style='Header.TLabel')
        header.pack(fill='x', ipady=10)
        
        # Main content frame
        content_frame = ttk.Frame(self.water_quality_frame)
        content_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Form frame
        form_frame = ttk.LabelFrame(content_frame, text="Water Test Results")
        form_frame.pack(fill='both', side='left', expand=True, padx=5, pady=5)
        
        # Form fields
        ttk.Label(form_frame, text="Water Source ID:", font=('Arial', 10, 'bold')).grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.source_id = ttk.Entry(form_frame, font=('Arial', 10))
        self.source_id.grid(row=0, column=1, padx=10, pady=5, sticky='ew')
        
        ttk.Label(form_frame, text="Location:", font=('Arial', 10, 'bold')).grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.water_location = ttk.Entry(form_frame, font=('Arial', 10))
        self.water_location.grid(row=1, column=1, padx=10, pady=5, sticky='ew')
        
        ttk.Label(form_frame, text="Test Date:", font=('Arial', 10, 'bold')).grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.test_date = ttk.Entry(form_frame, font=('Arial', 10))
        self.test_date.insert(0, datetime.now().strftime("%Y-%m-%d"))
        self.test_date.grid(row=2, column=1, padx=10, pady=5, sticky='ew')
        
        ttk.Label(form_frame, text="pH Level:", font=('Arial', 10, 'bold')).grid(row=3, column=0, sticky="w", padx=10, pady=5)
        self.ph_level = ttk.Entry(form_frame, font=('Arial', 10))
        self.ph_level.grid(row=3, column=1, padx=10, pady=5, sticky='ew')
        
        ttk.Label(form_frame, text="Turbidity (NTU):", font=('Arial', 10, 'bold')).grid(row=4, column=0, sticky="w", padx=10, pady=5)
        self.turbidity = ttk.Entry(form_frame, font=('Arial', 10))
        self.turbidity.grid(row=4, column=1, padx=10, pady=5, sticky='ew')
        
        # Submit button
        ttk.Button(form_frame, text="Submit Water Test", command=self.submit_water_test).grid(row=5, column=0, columnspan=2, pady=10)
        
        # Recent tests frame
        tests_frame = ttk.LabelFrame(content_frame, text="Recent Water Tests")
        tests_frame.pack(fill='both', side='right', expand=True, padx=5, pady=5)
        
        # Create a text widget for tests
        self.tests_text = tk.Text(tests_frame, height=20, width=40, font=('Arial', 10))
        scrollbar = ttk.Scrollbar(tests_frame, orient='vertical', command=self.tests_text.yview)
        self.tests_text.configure(yscrollcommand=scrollbar.set)
        
        self.tests_text.pack(side='left', fill='both', expand=True, padx=5, pady=5)
        scrollbar.pack(side='right', fill='y')
        
        # Configure grid weights
        form_frame.columnconfigure(1, weight=1)
        
    def create_alerts_tab(self):
        # Header
        header_frame = ttk.Frame(self.alerts_frame)
        header_frame.pack(fill='x', pady=10)
        
        header = ttk.Label(header_frame, text="Disease Outbreak Alerts", style='Header.TLabel')
        header.pack(fill='x', ipady=10)
        
        # Alerts list frame
        alerts_list_frame = ttk.LabelFrame(self.alerts_frame, text="Active Alerts")
        alerts_list_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Create a text widget for alerts
        self.alerts_text = tk.Text(alerts_list_frame, height=15, font=('Arial', 10))
        scrollbar = ttk.Scrollbar(alerts_list_frame, orient='vertical', command=self.alerts_text.yview)
        self.alerts_text.configure(yscrollcommand=scrollbar.set)
        
        self.alerts_text.pack(side='left', fill='both', expand=True, padx=5, pady=5)
        scrollbar.pack(side='right', fill='y')
        
        # Action buttons frame
        action_frame = ttk.Frame(self.alerts_frame)
        action_frame.pack(fill='x', padx=10, pady=10)
        
        ttk.Button(action_frame, text="Acknowledge Alert", command=self.acknowledge_alert).pack(side='left', padx=5)
        ttk.Button(action_frame, text="Send Response", command=self.send_response).pack(side='left', padx=5)
        ttk.Button(action_frame, text="Generate Report", command=self.generate_report).pack(side='left', padx=5)
        ttk.Button(action_frame, text="HealthPool_WEB", command=self.web_healthpool).pack(side='left', padx=5)
        ttk.Button(action_frame, text="ABOUT AEROPACE", command=self.abt_aeropace).pack(side='left', padx=5)
    def submit_health_data(self):
        # Collect data from form
        patient_id = self.patient_id.get()
        age = self.age.get()
        location = self.location.get()
        date = self.date.get()
        
        symptoms = []
        if self.fever.get(): symptoms.append("Fever")
        if self.diarrhea.get(): symptoms.append("Diarrhea")
        if self.vomiting.get(): symptoms.append("Vomiting")
        if self.dehydration.get(): symptoms.append("Dehydration")
        
        symptoms_str = ", ".join(symptoms) if symptoms else "None reported"
        
        # Add to data store
        self.symptoms_data.append({
            "id": patient_id,
            "age": age,
            "location": location,
            "date": date,
            "symptoms": symptoms_str
        })
        
        # Update entries text
        entry_text = f"ID: {patient_id}, Age: {age}, Location: {location}\nDate: {date}\nSymptoms: {symptoms_str}\n{'-'*40}\n"
        self.entries_text.insert('end', entry_text)
        
        # Check for potential alerts
        if "Diarrhea" in symptoms and "Vomiting" in symptoms:
            self.generate_alert(location, "Potential cholera case detected")
        
        # Clear form
        self.patient_id.delete(0, tk.END)
        self.age.delete(0, tk.END)
        self.location.delete(0, tk.END)
        
        # Update dashboard
        self.total_cases_label.config(text=str(len(self.symptoms_data)))
        
        messagebox.showinfo("Success", "Health data submitted successfully!")
        
    def submit_water_test(self):
        # Collect data from form
        source_id = self.source_id.get()
        location = self.water_location.get()
        test_date = self.test_date.get()
        ph_level = self.ph_level.get()
        turbidity = self.turbidity.get()
        
        # Add to data store
        self.water_quality_data.append({
            "source_id": source_id,
            "location": location,
            "date": test_date,
            "ph": ph_level,
            "turbidity": turbidity
        })
        
        # Update tests text
        test_text = f"Source: {source_id}, Location: {location}\nDate: {test_date}, pH: {ph_level}, Turbidity: {turbidity}\n{'-'*40}\n"
        self.tests_text.insert('end', test_text)
        
        # Check for potential alerts
        if float(ph_level) < 6.5 or float(ph_level) > 8.5:
            self.generate_alert(location, f"Abnormal pH level in water source {source_id}")
        if float(turbidity) > 5.0:
            self.generate_alert(location, f"High turbidity in water source {source_id}")
        
        # Clear form
        self.source_id.delete(0, tk.END)
        self.water_location.delete(0, tk.END)
        self.ph_level.delete(0, tk.END)
        self.turbidity.delete(0, tk.END)
        
        # Update dashboard
        self.water_tested_label.config(text=str(len(self.water_quality_data)))
        
        messagebox.showinfo("Success", "Water test data submitted successfully!")
        
    def generate_alert(self, location, message):
        severity = "High" if "cholera" in message.lower() or "high" in message.lower() else "Medium"
        date = datetime.now().strftime("%Y-%m-%d %H:%M")
        
        alert = {
            "date": date,
            "location": location,
            "severity": severity,
            "message": message
        }
        
        self.alerts.append(alert)
        
        # Update alerts listbox
        self.alerts_listbox.insert(tk.END, f"{date} - {location}: {message}")
        
        # Update alerts text
        alert_text = f"{date} - {location} ({severity}): {message}\n{'-'*60}\n"
        self.alerts_text.insert('end', alert_text)
        
        # Update dashboard
        self.active_alerts_label.config(text=str(len(self.alerts)))
        
    def acknowledge_alert(self):
        messagebox.showinfo("Alert Acknowledged", "Alert has been acknowledged and marked as reviewed")

    def web_healthpool(self): #ORIGINALLY OPENS THE WEBSITE!!!
        webbrowser.open("https://health-pool.tiiny.site/")
            
    def send_response(self):
        messagebox.showinfo("Response Sent", "Response has been sent to the relevant health authorities")
            
    def generate_report(self):
        messagebox.showinfo("Report Generated", "Outbreak report generated and sent to health authorities")

    def abt_aeropace(self): #ORIGINALLY OPENS THE WEBSITE, THEN THE WEBPAGE
        webbrowser.open("https://health-pool.tiiny.site/about.html")
        
    def generate_sample_data(self):
        # Generate sample health data
        sample_locations = ["Village A", "Village B", "Village C", "Village D"]
        sample_symptoms = ["Fever, Diarrhea", "Vomiting, Dehydration", "Fever, Vomiting", "Diarrhea"]
        
        for i in range(5):
            date = datetime(2023, random.randint(1, 12), random.randint(1, 28)).strftime("%Y-%m-%d")
            location = random.choice(sample_locations)
            symptoms = random.choice(sample_symptoms)
            
            self.symptoms_data.append({
                "id": f"P{1000 + i}",
                "age": str(random.randint(5, 70)),
                "location": location,
                "date": date,
                "symptoms": symptoms
            })
            
            # Add to entries text
            entry_text = f"ID: P{1000 + i}, Age: {random.randint(5, 70)}, Location: {location}\nDate: {date}\nSymptoms: {symptoms}\n{'-'*40}\n"
            self.entries_text.insert('end', entry_text)
            
            # Generate some alerts based on symptoms
            if "Diarrhea" in symptoms and random.random() > 0.7:
                self.generate_alert(location, "Multiple diarrhea cases reported")
        
        # Generate sample water quality data
        for i in range(4):
            date = datetime(2023, random.randint(1, 12), random.randint(1, 28)).strftime("%Y-%m-%d")
            location = random.choice(sample_locations)
            ph = round(random.uniform(6.0, 8.5), 1)
            turbidity = round(random.uniform(1.0, 10.0), 1)
            
            self.water_quality_data.append({
                "source_id": f"WS{200 + i}",
                "location": location,
                "date": date,
                "ph": ph,
                "turbidity": turbidity
            })
            
            # Add to tests text
            test_text = f"Source: WS{200 + i}, Location: {location}\nDate: {date}, pH: {ph}, Turbidity: {turbidity}\n{'-'*40}\n"
            self.tests_text.insert('end', test_text)
        
        # Generate a high turbidity alert
        self.generate_alert("Village B", "High turbidity in water source WS202")
        
        # Update dashboard statistics
        self.total_cases_label.config(text=str(len(self.symptoms_data)))
        self.active_alerts_label.config(text=str(len(self.alerts)))
        self.water_tested_label.config(text=str(len(self.water_quality_data)))
        self.high_risk_label.config(text="2")  # Sample value

def main():
    root = tk.Tk()
    app = HealthSurveillanceApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
