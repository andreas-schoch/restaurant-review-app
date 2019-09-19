import React from 'react';
import {  Link } from 'react-router-dom';
import './index.scss';
import { Button } from '../../styled'

// TODO replace button and input with styled components
const SearchHeader = (props) => {
    return (
        <div className='search-header'>
            <form className='search-header-form'>
                <input type='search'/>
                <Button>Search</Button>
            </form>
        </div>
    );
};

export default SearchHeader