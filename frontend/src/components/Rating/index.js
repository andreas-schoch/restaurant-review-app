import React from 'react';
import './index.scss';
import Header from '../Header'
import Footer from '../Footer'

const Rating = (props) => {


    return (
        <div className='rating-wrapper'>
            <i className="fas fa-star"> </i>
            <i className="fas fa-star"> </i>
            <i className="fas fa-star"> </i>
            <i className="fas fa-star"> </i>
            <i className="fas fa-star"> </i>
        </div>
    );
};

export default Rating;