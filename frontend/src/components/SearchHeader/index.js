import React from 'react';
import {  Link } from 'react-router-dom';
import './index.css';

// TODO replace button and input with styled components
const SearchHeader = (props) => {
    return (
        <div className='search-header'>
            <form className='search-header-form'>
                <input type='search'/>
                <button type='submit'>Search</button>
            </form>

        </div>
    );
};

export default SearchHeader