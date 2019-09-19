

const initial = {
    "1": {
        user: {
            first_name: "first",
            last_name: "last",
            username: "username",
            email: "email@example.com"
        },
        phone: "12345678",
        location: "Location",
        interests: "interests",
        bio: "my bio bla bla bla"
    },
    "2": {
        user: {
            first_name: "first",
            last_name: "last",
            username: "username",
            email: "email@example.com"
        },
        phone: "12345678",
        location: "Location",
        interests: "interests",
        bio: "my bio bla bla bla"
    },
    "3": {
        user: {
            first_name: "first",
            last_name: "last",
            username: "username",
            email: "email@example.com"
        },
        phone: "12345678",
        location: "Location",
        interests: "interests",
        bio: "my bio bla bla bla"
    },
    "4": {
        user: {
            first_name: "first",
            last_name: "last",
            username: "username",
            email: "email@example.com"
        },
        phone: "12345678",
        location: "Location",
        interests: "interests",
        bio: "my bio bla bla bla"
    },
};


export const userReducer = (users=initial, action) => {
    return users;
};

