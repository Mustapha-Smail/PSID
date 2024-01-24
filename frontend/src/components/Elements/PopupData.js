import { XCircleIcon } from "@heroicons/react/24/outline";
import { Button, Card, CardActions, CardContent, CardHeader, Divider, SvgIcon, Typography } from '@mui/material';
import { Stack } from '@mui/system';
import React from 'react';
import './PopupData.css';

const PopupData = ({ close, content, title }) => {
  return (
    <Card sx={{ width: '50%', borderRadius: '20px', height: '100%', boxShadow: '0px 5px 22px rgba(0, 0, 0, 0.04), 0px 0px 0px 0.5px rgba(0, 0, 0, 0.03)', display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
      <CardHeader
        title={title && title}
      />
      <CardContent>
        <Stack spacing={1} sx={{ width: '100%', height: '32rem', overflow: 'scroll' }}>
          <Typography>
            {content && content}
          </Typography>
        </Stack>
      </CardContent>
      <Divider />
      <CardActions sx={{ justifyContent: 'flex-end' }}>
        <Button
          color="inherit"
          endIcon={(
            <SvgIcon fontSize="small">
              <XCircleIcon />
            </SvgIcon>
          )}
          size="small"
          onClick={() => close()}
        >
          Fermer
        </Button>
      </CardActions>
    </Card>)
}

export default PopupData