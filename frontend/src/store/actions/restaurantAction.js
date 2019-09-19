import axios from "axios";
import { ERROR, SAVE_RESTAURANTS } from "../types";

const URL = `https://jable.co/`;

const objToArr = (obj) => Object.values(obj).map(item => item);


// backend returns arrays of objects. this transforms it into a single object with the id as key
const ArrToObj = (arr) => arr.reduce((acc, obj) => {
    acc[obj.id] = obj;
    return obj;
}, {});

export const saveRestaurants = (restaurants) => ({
    type: SAVE_RESTAURANTS,
    payload: { restaurants }
});

const error = error => {
  return {
    type: ERROR,
    payload: error
  };
};



export const saveRestaurantsAction = () => async dispatch => {
  try {
    const res = await axios.get(`${URL}api/restaurants/`);
    console.log(res.data);
    const restaurants = ArrToObj(res.data);

    dispatch(saveRestaurants(restaurants));
    return res;
  } catch (e) {
    dispatch(error("something went wrong"));
  }
};
