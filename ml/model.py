from numpy import power


class SolarWindModel:

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
        humidity = X[:, 6]
        wind_speed = X[:,7]
        rotor_area = X[:,8]


        performance_ratio =0.8

        System_capacity = (number_of_panels * panel_capacity) / 1000

        Energy = ( System_capacity * peak_sun_hours * performance_ratio * (1 - cloud_cover/100) * (radiation/1000) * (temperature/30) ) # Adjusting for temperature, assuming 30 degrees Celsius is optimal.

        # For wind energy, we would use a different formula that takes into account wind speed and 

        power_coefficient = 0.4 # typical value for modern wind turbines.
        air_density = 1.225 # kg/m^3
        
        Power = 0.5 * air_density * rotor_area * power_coefficient * wind_speed**3



        return Energy, Power # in kWh
    

    



        



        
    
    # computes the energy produced by the solar panels
    # based on the number of panels, panel capacity, peak sun hours, and perfomance ratio.
    # The energy is calculated using the formula:
    # Energy is in kilowatt-hours (kWh)
        


