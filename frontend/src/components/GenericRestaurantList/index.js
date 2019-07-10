import React, { useState } from 'react';
import RestaurantCard from "../RestaurantCard";



// this page was supposed to display the 4 best rated restaurants.
// but because we dont do reviews anymore, lets just show the 4 with the most comments.
// TODO create a container which filters the 4 most commented restaurants in the mapstatetoprops
const GenericRestaurantList = (props) =>  {
    return (
        <div className='generic-restaurant-list'>
            {props.restaurants.map((restaurant, i) => <RestaurantCard restaurant={restaurant} key={i} />)}
        </div>
    )
};


export default GenericRestaurantList;