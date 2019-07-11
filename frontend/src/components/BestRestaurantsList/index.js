import React from 'react';
import { connect } from 'react-redux';
import './index.scss';
import GenericRestaurantList from "../GenericRestaurantList";

const BestRestaurantsList = (props) =>  {
    console.log(props);
    return (
        <div className='best-restaurant-list'>
            <h2>Best Rated Restaurants</h2>
            <span className='best-restaurant-list-heading-underline'></span>
            <GenericRestaurantList restaurants={ props.restaurants }/>
        </div>
    )
};

const mapStateToProps = (state, propsSoFar) => {
    const getBestRestaurants = (restaurants, amount) => {
        // TODO refactor to filter the 4 best rated restaurants
        return Object.values(restaurants).map(restaurant => restaurant ).slice(0, amount);
    };

    return {
        'restaurants': getBestRestaurants(state.restaurantReducer, 4),
    }
};



export default connect(mapStateToProps)(BestRestaurantsList);