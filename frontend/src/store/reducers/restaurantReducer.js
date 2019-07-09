

const initial = {
    "1": {
        name: "restaurant name",
        category: "category",
        country: "country",
        street: "street",
        city: "city",
        zip: "zip",
        website: "website.com",
        phone: "12345678",
        email: "email@example.com",
        opening_hours: "Monday-Friday, 09:00-20:00",
        price_level: 3,
        restaurant_pic: "restaurant pic as base64 or url??"
    },
    "2": {
        name: "restaurant name",
        category: "category",
        country: "country",
        street: "street",
        city: "city",
        zip: "zip",
        website: "website.com",
        phone: "12345678",
        email: "email@example.com",
        opening_hours: "Monday-Friday, 09:00-20:00",
        price_level: 3,
        restaurant_pic: "restaurant pic as base64 or url??"
    },
    "3": {
        name: "restaurant name",
        category: "category",
        country: "country",
        street: "street",
        city: "city",
        zip: "zip",
        website: "website.com",
        phone: "12345678",
        email: "email@example.com",
        opening_hours: "Monday-Friday, 09:00-20:00",
        price_level: 3,
        restaurant_pic: "restaurant pic as base64 or url??"
    },
    "4": {
        name: "restaurant name",
        category: "category",
        country: "country",
        street: "street",
        city: "city",
        zip: "zip",
        website: "website.com",
        phone: "12345678",
        email: "email@example.com",
        opening_hours: "Monday-Friday, 09:00-20:00",
        price_level: 3,
        restaurant_pic: "restaurant pic as base64 or url??"
    },

};

export const restaurantReducer = (restaurants=initial, action) => {
    return restaurants;
};

