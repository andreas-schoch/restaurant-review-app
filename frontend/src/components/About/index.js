import React, { useEffect } from "react";
import { connect } from "react-redux";
import "./index.scss";
import { getMe } from "../../store/actions/meAction";
import { getComments } from "../../store/actions/commentsAction";


export function ProfileAbout (props) {
console.log()
    const me = props.me

    return (
<div className="profile-about">
        <div className="about-name">{me.username}</div>
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
          <li>{me.user_profile.member_since}</li>
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
       )
    }