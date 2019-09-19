import React, { useState } from 'react';
import './index.scss';
import { Link, Route, withRouter } from 'react-router-dom';
import SearchUsers from '../SearchUsers';
import SearchRestaurants from '../SearchRestaurants';
import SearchComments from '../SearchComments';
import RestaurantProfile from '../RestaurantProfile';

const SearchControls = (props) =>  {
    // state is necessary for the active tab styling (orange underline, font-weight)
    const [activeTab, setActiveTab] = useState(1);

    // reroute to one of the nested routes (usually happens only once)
    if (props.location.pathname === '/search') {
        props.history.push('/search/restaurants');
    }

    return (<>
        <div className='search-controls-nav-wrapper'>
            <form className='search-controls-form'>
                <input type='search' placeholder='Search'/>
                <select name="category ">
                    <option value="Asian">Asian</option>
                    <option value="Swiss">Swiss</option>
                    <option value="Italian">Italian</option>
                    <option value="Greek">Greek</option>
                </select>

            </form>
            <nav className={'search-controls-nav'}>
                <Link className={activeTab===1 ? 'nav-active' : ''} to={`/search/restaurants`} onClick={(e) => setActiveTab(1) }>Restaurants</Link>
                <Link className={activeTab===2 ? 'nav-active' : ''} to={`/search/comments`} onClick={(e) => setActiveTab(2) }>Comments</Link>
                <Link className={activeTab===3 ? 'nav-active' : ''} to={`/search/users`} onClick={(e) => setActiveTab(3) }>Users</Link>
            </nav>
        </div>

        <Route path={`${props.match.path}/restaurants`} exact component={ SearchRestaurants } />
        <Route path={`${props.match.path}/restaurants/:restaurant_id`} component={ withRouter(RestaurantProfile) } />
        <Route path={`${props.match.path}/comments`} component={ SearchComments } />
        <Route path={`${props.match.path}/users`} component={ SearchUsers } />
        </>
    )
};

export default SearchControls;