import axios from "axios";
import { COMMENTS } from "../types";
const URL = `https://jable.co/api/`;

export const comments = (data) => {
  return {
    type: COMMENTS,
    payload: data
  };
};
export const getComments = (idUser) => async (dispatch, getState ) => {
  const token = getState().loginReducer.token;
  const config = {
    headers: {
      Authorization: `Bearer ${token}`
    }
  };
  const response = await axios.get(`${URL}comments/user/1`, config);
  const data = response.data;
  dispatch(comments(data));
};
