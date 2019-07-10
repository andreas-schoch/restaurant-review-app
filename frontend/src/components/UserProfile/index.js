import React, { useEffect } from "react";
import { connect } from "react-redux";
import "./index.scss";
import { getMe } from "../../store/actions/meAction";


const UserProfile = ({ dispatch, me}) => {
    useEffect(() => {
        dispatch(getMe());
      }, []);

  return (
    <div className="profile-wrapper">
      <div className="profile-info">
        {/* left section */}
        <img
          className="profile-picture-me"
          src="./assets/img/default-profile-picture.jpg"
          alt=""
        />
        <p>User's Name</p>
        <ul>
          <li>Reviews</li>
          <li>Comments</li>
          <li>Restaurants</li>
          <li>EditProfile</li>
        </ul>
      </div>
      <div className="profile-reviews-me-list">
        <ul className="profile-short-info">
          <div className="profile-short-info-name">User's Name</div>
          <div className="profile-short-info-short">Zürich, ZH</div>
          <div className="profile-short-info-short">6 reviews</div>
          <div className="profile-short-info-short">210 Comments</div>
        </ul>
        <div className="profile-reviews-me">
          <div className="title">
            Läderach.. oder <p className="time">01.01.2018 15:22</p>
          </div>
          <li className="text">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam
            faucibus at odio id porta. Phasellus id sem augue. Donec non libero
            ut magna dignissim iaculis quis vitae tellus. Fusce a arcu
            fringilla, efficitur mi in, condimentum elit. Vestibulum eu arcu non
            purus sagittis varius. Vivamus at dolor a diam porttitor.
          </li>
        </div>
        <div className="profile-reviews-me">
          <div className="title">
            Läderach.. oder <p className="time">01.01.2018 15:22</p>
          </div>
          <li className="text">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam
            faucibus at odio id porta. Phasellus id sem augue. Donec non libero
            ut magna dignissim iaculis quis vitae tellus. Fusce a arcu
            fringilla, efficitur mi in, condimentum elit. Vestibulum eu arcu non
            purus sagittis varius. Vivamus at dolor a diam porttitor.
          </li>
        </div>
      </div>
      <div className="profile-about">
        <div className="about-name">About User</div>
        <div className="about-list">
          <li>
            <h2>Luna member since</h2>
          </li>
          <li>April, 2018</li>
        </div>
        <div className="about-list">
          <li>
            <h2>Luna member since</h2>
          </li>
          <li>April, 2018</li>
        </div>
        <div className="about-list">
          <li>
            <h2>Luna member since</h2>
          </li>
          <li>April, 2018</li>
        </div>
        <div className="about-list">
          <li>
            <h2>Luna member since</h2>
          </li>
          <li>April, 2018</li>
        </div>
      </div>
    </div>
  );
};

const mapStateToProps = (state) => {
    return {
        me: state.me.me,
        token: state.tokens.token
    };
};

export default connect(mapStateToProps) (UserProfile);
