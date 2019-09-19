import React from 'react';
import {  Link, withRouter } from 'react-router-dom';
import { connect } from 'react-redux';
import './index.scss';
import { Button } from '../../styled'
import RatingReadOnly from '../RatingReadOnly';
import CommentCardWide from '../CommentCardWide';
import CommentCardNarrow from '../CommentCardNarrow';

// TODO replace button and input with styled components
const RestaurantProfile = ({restaurant}) => {
    return (
        <div className='restaurant-profile'>
            <header className='restaurant-profile-header'>
                
                <div className='restaurant-profile-header-overlay'>
                <Link to="/search/restaurants"><i class="fas fa-arrow-left"></i> Back</Link>
                <div className='restaurant-profile-header-data'>
                    <h3>{restaurant.name}</h3>
                    <p>{restaurant.category}</p>
                    <div className='restaurant-profile-rating'>
                        <RatingReadOnly rating={restaurant.ratings_avg}/>
                        <span className='restaurant-profile-rating-count'>{restaurant.ratings_count + " reviews"}</span>
                    </div>
                </div>
                </div>
                <iframe width="360" height="360" id="gmap_canvas" src="https://maps.google.com/maps?q=propulsion%20academy&t=&z=13&ie=UTF8&iwloc=&output=embed" frameBorder="0" scrolling="no" marginHeight="0" marginWidth="0"></iframe>
            </header>
            <div className='restaurant-profile-body'>
                <div className="left">
                    <form>
                        <input type="search" placeholder='Filter List...' />
                        <Button className="filter-button">Filter</Button>
                    </form>
                    <CommentCardWide />
                    <CommentCardWide />
                    <CommentCardWide />
                    <CommentCardWide />
                    {/* <CommentCardNarrow /> */}
                </div>

                <div className="right">
                    <div className=''><i class="far fa-clock"></i> Monday - Friday 9:00 - 21:00</div>
                    <div><i class="far fa-money-bill-alt"></i> {`Price Level: ${"$$$"}`}</div>
                    <div className='restaurant-profile-btn-wrapper'>
                        <Button className="change-button">Write a Comment</Button>
                        <Button className="change-button">Edit Data</Button>
                    </div>
                </div>

            </div>
        </div>
    );
};


const mapStateToProps = (state, ownProps) => {
    return {
        'restaurant': state.restaurantReducer[ownProps.match.params.restaurant_id],
    }
};



export default withRouter(connect(mapStateToProps)(RestaurantProfile));
