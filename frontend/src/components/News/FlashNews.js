import { Link } from '@mui/material';
import React from 'react';
import './FlashNews.css';

const FlashNews = ({ text, url }) => {
    return (
        <div className="flash-news-container">
            <div className="flash-news">
                <span>
                    {text}
                </span>
                <span style={{ margin: '5px' }}>
                    <Link href={url}>
                        En savoir plus.
                    </Link>
                </span>
                <span>
                    {text}
                </span>
                <span style={{ margin: '5px' }}>
                    <Link href={url}>
                        En savoir plus.
                    </Link>
                </span>
            </div>
        </div>
    );
};

export default FlashNews;
