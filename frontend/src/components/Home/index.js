import React, { useState } from 'react';
import './index.css';

import RestaurantCard from '../RestaurantCard'
import SearchHeader from "../SearchHeader";
import BestRestaurantsList from "../BestRestaurantsList";

// this page was supposed to display the 4 best rated restaurants.
// but because we dont do reviews anymore, lets just show the 4 with the most comments.
const Home = (props) => <BestRestaurantsList />;


export default Home;