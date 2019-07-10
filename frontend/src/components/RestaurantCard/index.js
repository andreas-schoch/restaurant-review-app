import React, { useState } from 'react';
import { connect } from 'react-redux';
import './index.scss';
import Rating from "../Rating";
import Card from "../Card";
import {  Link } from 'react-router-dom';



function RestaurantCard(props) {
    const address = 'combine restaurant address';
  return (
    <Card>

    <div className='restaurant-card-wrap'>
        <Link to={'get-url-from-history'}>
          <div className='restaurant-card-pad'>
            <h3>{props.restaurant.name}</h3>
            <p>{address}</p>
            <Rating />
          </div>
            <img src='https://via.placeholder.com/270x280' alt='image of the restaurant'/>
        </Link>
    </div>
    </Card>
  );
}

export default RestaurantCard;
