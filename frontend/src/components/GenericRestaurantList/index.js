import React from 'react';
import './index.scss';
import RestaurantCard from "../RestaurantCard";

const GenericRestaurantList = (props) => (
    <div className='generic-restaurant-list'>
        {props.restaurants.map((restaurant, i) => <RestaurantCard restaurant={restaurant} key={i} />)}
    </div>
);


export default GenericRestaurantList;