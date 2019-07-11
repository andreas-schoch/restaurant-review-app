import React, { useEffect } from "react";
import { connect } from "react-redux";
import "./index.scss";
import { getMe } from "../../store/actions/meAction";
import { getComments } from "../../store/actions/commentsAction";


const UserProfile = ({ dispatch, me, comments}) => {
    useEffect(() => {
        dispatch(getMe());
        dispatch(getComments());
      }, []);

      let commentsArray;

  return (
    (me && comments && (
    <div className="profile-wrapper">
      <div className="profile-info">
        {/* left section */}
        <img
          className="profile-picture-me"
          src="./assets/img/default-profile-picture.jpg"
          alt=""
        />
        <p>{me.username}</p>
        <ul>
          <li>Comments</li>
          <li>Restaurants</li>
          <li>EditProfile</li>
        </ul>
      </div>
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
              <ul profile-reviews-me>
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
      <div className="profile-about">
        <div className="about-name">About {me.username}</div>
        <div className="about-list">
          <li>
            <h2>Location</h2>
          </li>
          <li>{me.user_profile.location}</li>
        </div>
        <div className="about-list">
          <li>
            <h2>Luna member since</h2>
          </li>
          <li>{me.user_prile.member_since}</li>
        </div>
        <div className="about-list">
          <li>
            <h2>Things I love</h2>
          </li>
          <li>{me.user_profile.interests}</li>
        </div>
        <div className="about-list">
          <li>
            <h2>Description</h2>
          </li>
          <li>{me.user_profile.bio}</li>
        </div>
      </div>
    </div>
    )) ||
    null
  );
};

const mapStateToProps = (state) => {
    return {
        me: state.meReducer.me,
        token: localStorage.token,
        comments: state.commentReducer.comments
    };
};

export default connect(mapStateToProps) (UserProfile);
