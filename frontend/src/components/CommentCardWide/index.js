import React from 'react';
import {  Link, withRouter } from 'react-router-dom';
import { connect } from 'react-redux';
import './index.scss';
import { Button } from '../../styled'
import RatingReadOnly from '../RatingReadOnly';
import moment from 'moment';



// TODO replace button and input with styled components
// TODO cleanup ghetto html + Css by adding classnames and splitting it up
const CommentCardWide = (props) => {
    const clickLikeHandler = (e) => {
        console.log("like");
    }
    return (
        <div className='comment-card-wide'>
            <header>
                <img src='/assets/img/derp.jpg'/>
                <div className='comment-card-wide-name-wrap'>
                    <h4 className='comment-card-wide-name'>Firstname L.</h4>
                    <p> 32 comments in total</p>
                </div>
                <RatingReadOnly  className='rating' rating={3}/>
                {/* <span className='comment-card-wide-created'>{moment(Date.now()).fromNow()}</span> */}
            </header>
            <section>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc faucibus luctus ultrices. Quisque at nunc risus. In elementum faucibus velit, a dapibus tortor ullamcorper tristique. Nam congue pharetra suscipit. Aliquam erat volutpat. Nullam non odio lacus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.
            </section>
            <footer>
                <button onClick={ clickLikeHandler }><i class="fas fa-thumbs-up"></i> {`Like ${40}`}</button>
            </footer>
        </div>
    );
};


export default connect()(CommentCardWide);
