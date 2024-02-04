import { Button, CircularProgress, Grid, SvgIcon } from '@mui/material';
import { Stack } from '@mui/system';
import axios from 'axios';
import React, { useEffect, useState } from 'react'
import './MLContainer.css'
import RestaurantCard from './RestaurantCard';
import SkipNextIcon from '@mui/icons-material/SkipNext';
import SkipPreviousIcon from '@mui/icons-material/SkipPrevious';

const MLContainer = ({
    fetchRestaurants,
    loading,
    restaurants,
    current,
    totalPages,
}) => {

    const [currentPage, setCurrentPage] = useState(current)


    useEffect(() => {
        fetchRestaurants(currentPage);
    }, [currentPage]);

    return (
        <>
            <h1>Recommended Restaurants</h1>
            {loading ?
                <Stack p={5} alignItems={"center"} >
                    <CircularProgress />
                </Stack> :
                <Grid container spacing={2} p={5}>
                    <Grid container spacing={2} lg={12} sx={{ display: 'flex', flexDirection: 'row' }}>
                        {restaurants.map((restaurant, index) => (
                            <RestaurantCard restaurant={restaurant} key={index} />
                        ))}
                    </Grid>
                    <Grid spacing={2} lg={12} sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
                        <Button
                            color="inherit"
                            endIcon={(
                                <SvgIcon fontSize="small">
                                    <SkipPreviousIcon />
                                </SvgIcon>
                            )}
                            size="small"
                            onClick={() => setCurrentPage(currentPage - 1)}
                            disabled={currentPage <= 1}
                        >
                            Previous
                        </Button>
                        <span> Page {currentPage} of {totalPages} </span>
                        <Button
                            color="inherit"
                            startIcon={(
                                <SvgIcon fontSize="small">
                                    <SkipNextIcon />
                                </SvgIcon>
                            )}
                            size="small"
                            onClick={() => setCurrentPage(currentPage + 1)}
                            disabled={currentPage >= totalPages}
                        >
                            Next
                        </Button>
                    </Grid>
                </Grid>
            }
        </>
    );
}

export default MLContainer