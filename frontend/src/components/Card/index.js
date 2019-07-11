import React from 'react';
import './index.scss';


const Card = (props) => (
    <div className='card-base'>
        {props.children}
    </div>
  );

export default Card;
