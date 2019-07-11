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
                <RatingReadOnly  className='rating' rating={props.comment.rating}/>
                {/* <span className='comment-card-wide-created'>{moment(Date.now()).fromNow()}</span> */}
            </header>
            <section>
                { props.comment.body}
            </section>
            <footer>
                <button onClick={ clickLikeHandler }><i class="fas fa-thumbs-up"></i> {`Like ${props.comment.likes_counter}`}</button>
            </footer>
        </div>
    );
};


export default connect()(CommentCardWide);
