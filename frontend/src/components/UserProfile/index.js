import React, { useEffect } from "react";
import { connect } from "react-redux";
import "./index.scss";
import { getMe } from "../../store/actions/meAction";
import { getComments } from "../../store/actions/commentsAction";
import {CommmentCom} from '../Comments'
import {ProfileAbout} from '../About'
import {ProfileInfo} from '../ProfileInfo'


const UserProfile = ({ dispatch, me, comments}) => {
    useEffect(() => {
        dispatch(getMe());
        dispatch(getComments());
      }, []);

      let commentsArray;

  return (
    (me && comments && (
    <div className="profile-wrapper">
      <ProfileInfo me={me} /> 
      <CommmentCom com={comments} me={me}/>
      <ProfileAbout me={me} />
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
