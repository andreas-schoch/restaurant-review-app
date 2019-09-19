import React from 'react';
import {  Link, withRouter } from 'react-router-dom';
import { connect } from 'react-redux';
import './index.scss';
import Card from '../Card';
import CommentCardWide from '../CommentCardWide';

const CommentCardNarrow = (props) => {
    return (
        <div className='comment-card-narrow'>
            <Card>
                <CommentCardWide comment={props.comment} />
            </Card>
        </div>
    );
};

export default connect()(CommentCardNarrow);
