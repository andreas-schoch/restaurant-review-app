import React, { useState } from 'react';
import { connect } from 'react-redux';

import RestaurantCard from '../RestaurantCard'
import SearchHeader from "../SearchHeader";
import GenericRestaurantList from "../GenericRestaurantList";

// this page was supposed to display the 4 best rated restaurants.
// but because we dont do reviews anymore, lets just show the 4 with the most comments.
// TODO create a container which filters the 4 most commented restaurants in the mapstatetoprops
const BestRestaurantsList = (props) =>  {
    return (
        <>
            <SearchHeader/>
            <h2>Best Rated Restaurants</h2>
            <GenericRestaurantList restaurants={ props.restaurants }/>
        </>
    )
};


const mapStateToProps = (state, propsSoFar) => {
    const getBestRestaurants = (restaurants, amount) => {
        // TODO refactor when backend available to filter the most commented restaurants or something.
        return Object.values(restaurants).map(restaurant => restaurant ).slice(0, amount);
    };

    return {
        'restaurants': getBestRestaurants(state.restaurants, 4),
    }
};



export default connect(mapStateToProps)(BestRestaurantsList);