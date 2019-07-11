import axios from "axios";
import { COMMENTS } from "../types";
const URL = `https://jable.co/api/`;

export const comments = (data) => {
  return {
    type: COMMENTS,
    payload: data
  };
};
export const getComments = () => async (dispatch, getState) => {
  const token = getState().loginReducer.token;
  const id = getState().meReducer.me.user_profile.id;
  const config = {
    headers: {
      Authorization: `Bearer ${token}`
    }
  };
  const response = await axios.get(`${URL}comments/${id}`, config);
  const data = response.data;
  dispatch(comments(data));
};
