import pandas as pd

House = {
    'Area': [50, 60, 80, 100, 120, 150, 40, 70, 90, 110],          
    'Bed': [1, 2, 2, 3, 3, 4, 1, 2, 3, 3],                        
    'Age': [10, 5, 15, 20, 2, 5, 25, 8, 12, 6],                   
    'Price': [1.5, 2.0, 2.5, 3.5, 4.2, 5.5, 1.2, 2.3, 3.0, 3.8]
}

df = pd.DataFrame(House)

df.to_csv('house_data.csv', index = False)

print (df)