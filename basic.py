def savings(gross_pay, tax_rate, expenses):
   import math

   savings = math.floor(gross_pay * (1 - tax_rate)) - expenses
   return savings

def material_waste(total_material, material_units, num_jobs, job_consumption):
    material_waste = total_material - (num_jobs * job_consumption)
    return str(material_waste) + material_units

def interest(principal, rate, periods):
    import math
   
    fv = principal + math.floor(principal * (rate * periods))
    return fv

def body_mass_index(weight, height):
    kg = weight / 2.205
    meters = ((height[0] * 12) + height[1]) / 39.37
    bmi = kg / (meters ** 2)
    return bmi
