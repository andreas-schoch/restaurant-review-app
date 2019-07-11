import React from 'react';
import {  Link } from 'react-router-dom';
import './index.scss';
import { Button } from '../../styled'

// TODO replace button and input with styled components
const RestaurantProfile = ({restaurant}) => {
    return (
        <div className='restaurant-profile'>
            Rest Profile
            <iframe width="360" height="360" id="gmap_canvas" src="https://maps.google.com/maps?q=propulsion%20academy&t=&z=13&ie=UTF8&iwloc=&output=embed" frameBorder="0" scrolling="no" marginHeight="0" marginWidth="0"></iframe>

        </div>
    );
};

export default RestaurantProfile;