import React  from 'react';
import './index.scss';
import { Route } from 'react-router-dom';
import SearchRestaurants from "../SearchRestaurants";
import SearchNavigation from "../SearchControls";
import SearchComments from "../SearchComments";
import SearchUsers from "../SearchUsers";

const Search = (props) =>  {
    return (
        <>
            <SearchNavigation/>

            <Route  path='/search/restaurants'  component={ SearchRestaurants } />
            <Route  path='/search/comments'  component={ SearchComments } />
            <Route  path='/search/users'  component={ SearchUsers } />

        </>
    )
};

export default Search;