import React from 'react';
import './index.scss';
import Header from '../Header'
import Footer from '../Footer'

const App = (props) => {
    return (
        <div className='content-wrapper'>
            <Header className='main-header'/>
            <span className='content'>{ props.children }</span>
            <Footer className={'main-footer'}/>
        </div>
    );
};

export default App;