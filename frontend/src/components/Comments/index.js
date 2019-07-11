import React, { useEffect } from "react";
import { connect } from "react-redux";
import "./index.scss";
import { getMe } from "../../store/actions/meAction";
import { getComments } from "../../store/actions/commentsAction";


export function CommmentCom (props) {
console.log()
    const me = props.me
    const comments = props.com

    return (
        <div className="profile-reviews-me-list">
                <ul className="profile-short-info">
                <div className="profile-short-info-name">{me.username}</div>
                <div className="profile-short-info-short">{me.user_profile.location}</div>
                <div className="profile-short-info-short">3 Comments</div>
                </ul>
                <div className="profile-reviews-me">
                {Object.values(comments).map((i, index) => {
                console.log(i);
                return (
                    <div key={index}>
                    <ul className='profile-reviews-me'>
                        <li>{i.body}</li>
                        <li>{i.rating}</li>
                        <li>{i.created}</li>
                        <li>{i.restaurant.name}</li>
                    </ul>
                    </div>
                );
                })}
                <li className="text">
                    {comments.body}
                </li>
                </div>
            </div>
    )
}