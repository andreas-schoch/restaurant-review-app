import React, { useState } from 'react';
import { connect } from 'react-redux';
import './index.css';


function RestaurantCard(props) {
    const address = 'combine restaurant address'
  return (
    <div className='restaurant-card'>
        <h3>{props.restaurant.name}</h3>
        <p>{address}</p>
        <div>placeholder</div>
        <img src='https://via.placeholder.com/250x250' alt='image of the restaurant'/>
    </div>
  );
}

export default RestaurantCard;
