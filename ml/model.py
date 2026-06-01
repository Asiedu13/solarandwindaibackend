class SolarModel:

    def predict(self,X):

        """Predicts the energy produced by solar panels based on weather data and system paramters."""

        import numpy as np
        X = np.array(X)

        temperature = X[:, 0]
        cloud_cover = X[:, 1]
        radiation = X[:, 2]
        number_of_panels = X[:, 3]
        panel_capacity = X[:, 4]
        peak_sun_hours = X[:, 5]

        performance_ratio =0.8

        System_capacity = (number_of_panels * panel_capacity) / 1000

        Energy = ( System_capacity * peak_sun_hours * performance_ratio * (1 - cloud_cover/100) * (radiation/1000) * (temperature/30) ) # Adjusting for temperature, assuming 30 degrees Celsius is optimal.

        return Energy # in kWh


        



        System_capacity = (Number_of_Panels * Panel_Capacity) /1000
        Energy = System_capacity * Peak_sun_hours * Performance_ratio * (1 - cloud_cover/100) * (radiation/1000) * (temperature/30) # Adjusting for temperature, assuming 30 degrees Celsius is optimal.
        return Energy # in kWh
    
    # computes the energy produced by the solar panels
    # based on the number of panels, panel capacity, peak sun hours, and perfomance ratio.
    # The energy is calculated using the formula:
    # Energy is in kilowatt-hours (kWh)
        


