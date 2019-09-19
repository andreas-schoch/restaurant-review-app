import React from 'react';
import './index.scss';
import Card from "../Card";
import {  Link, withRouter } from 'react-router-dom';
import RatingReadOnly from '../RatingReadOnly';

function RestaurantCard({restaurant, match}) {
    const address = `${restaurant.street}, ${restaurant.city} ${restaurant.zip}, ${restaurant.country}`;
  return (
    <Card>
      <div className='restaurant-card-wrap'>
          <Link to={`/search/restaurants/${restaurant.id}`}>
            <div className='restaurant-card-pad'>
              <h3>{restaurant.name}</h3>
              <p>{address}</p>

              <div className='restaurant-card-rating'>
                <RatingReadOnly rating={restaurant.ratings_avg}/>
                <span className='restaurant-card-rating-count'>{restaurant.ratings_count}</span>
              </div>

            </div>
            <img src='https://via.placeholder.com/270x680' alt='image of the restaurant'/>
          </Link>
      </div>
    </Card>
  );
}

export default withRouter(RestaurantCard);
