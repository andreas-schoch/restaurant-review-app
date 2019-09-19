import React, { useState, useEffect } from 'react';
import './index.scss';
import Rating from 'react-rating'


const RatingReadOnly = (props) => (
    <Rating
        emptySymbol="fas fa-star star-empty"
        fullSymbol="fas fa-star star-full"
        readonly
        fractions={2}
        initialRating={props.rating}
    />
);


export default RatingReadOnly;