ports_car_dataset = {
    "Porsche 911": {"Body Type": "Coupe", "Engine": "Gasoline"},
    "Chevrolet Corvette": {"Body Type": "Coupe", "Engine": "Gasoline"},
    "Nissan GT-R": {"Body Type": "Coupe", "Engine": "Gasoline"},
    "Audi R8": {"Body Type": "Coupe", "Engine": "Gasoline"},
    "Ford Mustang Shelby GT500": {"Body Type": "Coupe", "Engine": "Gasoline"},
    "Ferrari 488": {"Body Type": "Coupe", "Engine": "Gasoline"},
    "Lamborghini Huracan": {"Body Type": "Coupe", "Engine":"Gasoline"},
    "McLaren": {"Body Type": "Coupe", "Engine": "Gasoline"},
    "BMW M4": {"Body Type": "Coupe", "Engine": "Gasoline"}
}

def recommend_sports_cars(user_preferences):
    recommended_cars = []
    for car, features in sports_car_dataset.items():
        common_features = set(features.values()) & set(user_preferences)
        similarity_score = len(common_features) / len(user_preferences)
        
        
        if similarity_score > 0:
            recommended_cars.append((car, similarity_score))
    
    recommended_cars.sort(key=lambda x: x[1], reverse=True)
    
    return recommended_cars

user_preferences = ["Coupe", "Gasoline"]
recommendations = recommend_sports_cars(user_preferences)
print("Recommended sports cars based on your preferences:")
for car, score in recommendations:
    print(f"- {car} (Similarity Score: {score})")
