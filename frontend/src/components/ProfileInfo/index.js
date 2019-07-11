import React, { useEffect } from "react";
import { connect } from "react-redux";
import "./index.scss";
import { getMe } from "../../store/actions/meAction";
import { getComments } from "../../store/actions/commentsAction";


export function ProfileInfo (props) {
console.log()
    const me = props.me

    return (
<div className="profile-info">
        {/* left section */}
        <img
          className="profile-picture-me"
          src="./assets/img/default-profile-picture.jpg"
          alt=""
        />
        <p>{me.username}</p>
        <ul className='buttonProfile'>
          <button>Comments</button>
          <button>Restaurants</button>
          <button>EditProfile</button>
        </ul>
      </div>
      )
    }