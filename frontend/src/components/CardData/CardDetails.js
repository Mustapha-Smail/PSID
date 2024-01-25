import { Alert, CircularProgress, Grid } from '@mui/material'
import { Stack } from '@mui/system'
import axios from 'axios'
import React, { useEffect, useState } from 'react'
import CardData from './CardData'
import RestaurantIcon from '@mui/icons-material/Restaurant';
import CommentIcon from '@mui/icons-material/Comment';
import ReviewsIcon from '@mui/icons-material/Reviews';
import LocalFloristIcon from '@mui/icons-material/LocalFlorist';
import LocalDiningIcon from '@mui/icons-material/LocalDining';
import NoMealsIcon from '@mui/icons-material/NoMeals';

const CardDetails = ({ url }) => {
    const [data, setData] = useState(null)
    const [loading, setLoading] = useState(false)
    const [error, setError] = useState(null)

    useEffect(() => {
        const getData = async () => {
            try {
                setLoading(true)
                const { data } = await axios.get(`${url}`)
                setData(data)
                setLoading(false)
            } catch (err) {
                setLoading(false)
                setError(err)
                console.error(err)
            }
        }

        getData()
    }, [url])

    const getIconForTitle = (title) => {
        switch (title) {
            case "Restaurants":
                return <RestaurantIcon />;
            case "Note moyenne":
                return <ReviewsIcon />
            case "Commentaires":
                return <CommentIcon />
            case "Végétarien":
                return <LocalFloristIcon />
            case "Vegan":
                return <LocalDiningIcon />;
            case "Sans gluten":
                return <NoMealsIcon />;
            default:
                return null; // Default case if no match
        }
    };

    return (
        <Grid container spacing={2} px={3}>
            {error && <Alert severity="error">{error.message}</Alert>}
            {loading ?
                <Stack p={5} alignItems={"center"} >
                    <CircularProgress />
                </Stack>
                : data && data.map((d, key) => (
                    <Grid md={2} key={key}>
                        <CardData
                            title={d.title}
                            value={d.value}
                        >
                            {getIconForTitle(d.title)}
                        </CardData>
                    </Grid>
                ))}
        </Grid>
    )
}

export default CardDetails