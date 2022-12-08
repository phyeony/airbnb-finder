import {
  Button,
  FormLabel,
  FormControl,
  FormGroup,
  FormControlLabel,
  FormHelperText,
  Checkbox,
  Stack,
  Card,
  CardHeader,
  CardContent,
  Divider,
  List,
  ListItem,
  ListItemIcon,
  ListItemText,
  Grid,
  Box,
  TextField,
  Typography,
  Link
} from "@mui/material";

import { useState } from "react";

function not(a, b) {
  return a.filter((value) => b.indexOf(value) === -1);
}

function intersection(a, b) {
  return a.filter((value) => b.indexOf(value) !== -1);
}

function union(a, b) {
  return [...a, ...not(b, a)];
}

function App() {
  const PUBLIC_TRANSPORTATION = "Public Transportation"
  const TOURISM_CULTURE = "Tourism & Culture"
  const MAX_NUM = 20000
  const URL = process.env.REACT_APP_ENV === "railway" ? `https://${process.env.REACT_APP_BACKEND_DOMAIN}` : 'http://localhost:8000'

  const [airbnbList, setAirbnbList] = useState([])
  const [state, setState] = useState({
    entire: false,
    pv: false,
    shared: false,
    hotel: false,
  });
  const [roomTypeError, setRoomTypeError] = useState(false)

  const handleChange = (event) => {
    setState({
      ...state,
      [event.target.name]: event.target.checked,
    });
  };


  const { entire, pv, shared, hotel } = state;

  const handleSubmit = async () => {
    // Iterate through the object
    let airbnb_room_type = []
    for (const key in state) {
      if (state[key]) {
        let name;
        switch(key) {
          case 'entire':
            name = 'Entire home/apt'
            break;
          case 'pv':
            name = 'Private room'
            break;
          case 'shared':
            name = 'Shared room'
            break;
          case 'hotel':
            name = 'Hotel room'
            break; 
          default:
            break;//do nothing
        }
        airbnb_room_type.push(name)
      }
    }
    if(airbnb_room_type.length === 0) {
      setRoomTypeError(true)
      return
    } else {
      setRoomTypeError(false)
    }
    try {
      const res = await fetch(`${URL}/api/airbnb_list`, {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          min_price: minPrice ?? 0,
          max_price: maxPrice ?? MAX_NUM,
          activity_preference: right.map((activity) => {
            if (activity === PUBLIC_TRANSPORTATION) {
              return 'transportation'
            } else if (activity === TOURISM_CULTURE) {
              return 'tourism'
            }
            return activity.toLowerCase()
          }),
          airbnb_room_type,
        }) 
      })

      if (res.status === 200) {
        const data = await res.json()
        setAirbnbList(data)
      }


    } catch(e) {
      console.error(e)
    }
  };

  const [minPrice, setMinPrice] = useState(null);
  const [maxPrice, setMaxPrice] = useState(null);

  const [error, setError] = useState(false);
  const [errorMessage, setErrorMessage] = useState("");

  const [maxError, setMaxError] = useState(false);
  const [maxErrorMessage, setMaxErrorMessage] = useState("");

  const HandleMinPriceChange = (inputString) => {
    var numbers = /^[0-9]+$/;
    if (inputString.match(numbers)) {
      const temp_min = parseInt(inputString)
      if(maxPrice && temp_min > maxPrice){
        setErrorMessage("Min Price can't be bigger than Max Price");
        setError(true);
        return
      } else if(temp_min > MAX_NUM) {
        setErrorMessage("Too expensive! The highest airbnb price is $13025 CAD.");
        setError(true);
        return
      }
      setError(false);
      setErrorMessage("");
      setMinPrice(temp_min);
    } else {
      setErrorMessage("Please input numbers only");
      setError(true);
    }
  };

  const HandleMaxPriceChange = (inputString) => {
    var numbers = /^[0-9]+$/;
    if (inputString.match(numbers)) {
      const temp_max = parseInt(inputString)
      if(minPrice && minPrice > temp_max){
        setMaxErrorMessage("Min Price can't be bigger than Max Price");
        setMaxError(true);
        return
      } else if(temp_max > MAX_NUM) {
        setMaxErrorMessage("Too expensive! The highest airbnb price is $13025 CAD.");
        setMaxError(true);
        return
      }
      setMaxError(false);
      setMaxErrorMessage("");
      setMaxPrice(temp_max);
    } else {
      setMaxErrorMessage("Please input numbers only");
      setMaxError(true);
    }
  };

  const [checked, setChecked] = useState([]);
  const [left, setLeft] = useState([
    "Entertainment", "Food", "Leisure", PUBLIC_TRANSPORTATION, "Shop", TOURISM_CULTURE
  ]);
  const [right, setRight] = useState([]);

  const leftChecked = intersection(checked, left);
  const rightChecked = intersection(checked, right);

  const handleToggle = (value) => () => {
    const currentIndex = checked.indexOf(value);
    const newChecked = [...checked];

    if (currentIndex === -1) {
      newChecked.push(value);
    } else {
      newChecked.splice(currentIndex, 1);
    }

    setChecked(newChecked);
  };

  const numberOfChecked = (items) => intersection(checked, items).length;

  const handleToggleAll = (items) => () => {
    if (numberOfChecked(items) === items.length) {
      setChecked(not(checked, items));
    } else {
      setChecked(union(checked, items));
    }
  };

  const handleCheckedRight = () => {
    setRight(right.concat(leftChecked));
    setLeft(not(left, leftChecked));
    setChecked(not(checked, leftChecked));
  };

  const handleCheckedLeft = () => {
    setLeft(left.concat(rightChecked));
    setRight(not(right, rightChecked));
    setChecked(not(checked, rightChecked));
  };

  const customList = (title, items) => (
    <Card>
      <CardHeader
        sx={{ px: 2, py: 1 }}
        avatar={
          <Checkbox
            onClick={handleToggleAll(items)}
            checked={
              numberOfChecked(items) === items.length && items.length !== 0
            }
            indeterminate={
              numberOfChecked(items) !== items.length &&
              numberOfChecked(items) !== 0
            }
            disabled={items.length === 0}
            inputProps={{
              "aria-label": "all items selected",
            }}
          />
        }
        title={title}
        subheader={`${numberOfChecked(items)}/${items.length} selected`}
      />
      <Divider />
      <List
        sx={{
          width: 200,
          height: 230,
          bgcolor: "background.paper",
          overflow: "auto",
        }}
        dense
        component="div"
        role="list"
      >
        {items.map((value) => {
          const labelId = `transfer-list-all-item-${value}-label`;

          return (
            <ListItem
              key={value}
              role="listitem"
              button
              onClick={handleToggle(value)}
            >
              <ListItemIcon>
                <Checkbox
                  checked={checked.indexOf(value) !== -1}
                  tabIndex={-1}
                  disableRipple
                  inputProps={{
                    "aria-labelledby": "labelId",
                  }}
                />
              </ListItemIcon>
              <ListItemText id={labelId} primary={value} />
            </ListItem>
          );
        })}
        <ListItem />
      </List>
    </Card>
  );

  return (
    <Stack alignItems="center" justifyContent="space-evenly" spacing={2}>
      <Typography variant="h3">Airbnb Finder</Typography>
      <FormControl component="fieldset" variant="standard">
        <FormLabel component="legend" error={roomTypeError} required>1. Select Your Room Type (Please select at least 1)</FormLabel>
        <FormGroup>
          <FormControlLabel
            control={
              <Checkbox
                checked={entire}
                onChange={handleChange}
                name="entire"
              />
            }
            label="Entire home/apt"
          />
          <FormControlLabel
            control={
              <Checkbox checked={pv} onChange={handleChange} name="pv" />
            }
            label="Private room"
          />
          <FormControlLabel
            control={
              <Checkbox
                checked={shared}
                onChange={handleChange}
                name="shared"
              />
            }
            label="Shared room"
          />
          <FormControlLabel
            control={
              <Checkbox
                checked={hotel}
                onChange={handleChange}
                name="hotel"
              />
            }
            label="Hotel room"
          />
        </FormGroup>
        {roomTypeError && <FormHelperText error>Must select at least 1 room type</FormHelperText>}
        <FormLabel component="legend" sx={{mt:1}}>2. Select Your Price Range</FormLabel>
        <Box
          component="form"
          sx={{
            "& > :not(style)": { m:2, width: "25ch" },
          }}
          noValidate
          autoComplete="off"
        >
          <TextField
            id="min price"
            label="Min Price ($CAD)"
            onChange={(e) => HandleMinPriceChange(e.target.value)}
            error={error}
            helperText={errorMessage}
          />
          <TextField
            id="max price"
            label="Max Price ($CAD)"
            onChange={(e) => HandleMaxPriceChange(e.target.value)}
            error={maxError}
            helperText={maxErrorMessage}
          />
        </Box>

        <FormLabel component="legend" sx={{mt:1, mb:1}}>
          3. Preference - Choose items in order of your importance{" "}
        </FormLabel>
        <Grid container spacing={2} justifyContent="center" alignItems="center">
          <Grid item>{customList("Choices", left)}</Grid>
          <Grid item>
            <Grid container direction="column" alignItems="center">
              <Button
                sx={{ my: 0.5 }}
                variant="outlined"
                size="small"
                onClick={handleCheckedRight}
                disabled={leftChecked.length === 0}
                aria-label="move selected right"
              >
                &gt;
              </Button>
              <Button
                sx={{ my: 0.5 }}
                variant="outlined"
                size="small"
                onClick={handleCheckedLeft}
                disabled={rightChecked.length === 0}
                aria-label="move selected left"
              >
                &lt;
              </Button>
            </Grid>
          </Grid>
          <Grid item>{customList("Chosen", right)}</Grid>
        </Grid>
      </FormControl>
      <Button variant="contained" onClick={handleSubmit} disabled={error || maxError}>
        Find!
      </Button>

      {
        airbnbList.map((airbnb, idx) =>
          <Card key={idx} sx={{ width: 1 / 1.5, maxWidth: 500 }}>
            <CardContent>
              <Stack direction="row" justifyContent="space-between" sx={{ mb: 1 }}>
                <Typography variant="h6" component="div">
                  {airbnb.name}
                </Typography>
                <Stack alignItems='flex-end'>
                  <Typography noWrap variant="h6" component="div">
                    ${airbnb.price} CAD
                  </Typography>
                  <Typography align="right" variant="subtitle" display="inline" component="span">
                    night
                  </Typography>
                </Stack>
              </Stack>
              <Link href={airbnb.listing_url} rel="noopener" target="_blank" underline="always">
                {airbnb.listing_url}
              </Link>

              <Stack direction="row" alignItems='center' sx={{mt:1}}>
                <Typography variant="body1">
                  Airbnb Review Rating:
                </Typography>
                <Typography variant="h6" sx={{ml:1}}>
                  {airbnb.review_scores_rating}
                </Typography>
              </Stack>
            </CardContent>
          </Card>
        )

      }
    </Stack>
  );
}

export default App;
