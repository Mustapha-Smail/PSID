import { Button, Card, CardActions, CardContent, CardMedia, Grid, SvgIcon, Typography } from '@mui/material';
import React from 'react'
import StarIcon from '@mui/icons-material/Star';
const RestaurantCard = ({ restaurant }) => {
    return (
        <Grid lg={3} md={4} sm={12} p={2}>
            <Card>
                {/* <CardMedia
                    sx={{ height: 140 }}
                    image="/static/images/cards/contemplative-reptile.jpg"
                    title="green iguana"
                /> */}
                <CardContent>
                    <Typography gutterBottom variant="h4" component="div">
                        {restaurant.restaurant_name}
                    </Typography>
                    <Typography variant="h6" color="div">
                        Moyenne: {restaurant.avg_rating}
                        <StarIcon color='warning' />
                    </Typography>
                    <Typography variant="body2" color="text.secondary">
                        {restaurant.address}
                    </Typography>
                </CardContent>
                <CardActions>
                    <Button size="small" href={`https://www.tripadvisor.fr/Restaurant_Review-${restaurant.restaurant_link}`} target="_blank">Voir</Button>
                </CardActions>
            </Card>
        </Grid>
    );

}

export default RestaurantCard