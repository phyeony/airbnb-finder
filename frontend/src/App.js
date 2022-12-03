import {
  Button,
  FormLabel,
  FormControl,
  FormGroup,
  FormControlLabel,
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
  const [airbnbList, setAirbnbList] = useState([])
  const [state, setState] = useState({
    entire: false,
    pv: false,
    shared: false,
  });

  const handleChange = (event) => {
    setState({
      ...state,
      [event.target.name]: event.target.checked,
    });
  };

  const { entire, pv, shared } = state;

  const handleSubmit = async () => {
    // Iterate through the object
    let airbnb_room_type = []
    for (const key in state) {
      if (state[key]) {
        airbnb_room_type.push(key)
      }
    }
    try {
      const res = await fetch("http://localhost:8000/api/airbnb_list", {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          airbnb_price_range: [minprice, maxprice],
          airbnb_room_type,
          activity_preference: right
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

  const [minprice, setMinPrice] = useState(0);
  const [maxprice, setMaxPrice] = useState(0);

  const [error, setError] = useState(false);
  const [errorMessage, setErrorMessage] = useState("");

  const [maxError, setMaxError] = useState(false);
  const [maxErrorMessage, setMaxErrorMessage] = useState("");

  const HandleMinPriceChange = (inputString) => {
    var numbers = /^[0-9]+$/;
    if (inputString.match(numbers)) {
      setError(false);
      setErrorMessage("");
      setMinPrice(inputString);
    } else {
      setErrorMessage("Please input numbers only");
      setError(true);
    }
  };

  const HandleMaxPriceChange = (inputString) => {
    var numbers = /^[0-9]+$/;
    if (inputString.match(numbers)) {
      setMaxError(false);
      setMaxErrorMessage("");
      setMaxPrice(inputString);
    } else {
      setMaxErrorMessage("Please input numbers only");
      setMaxError(true);
    }
  };

  const [checked, setChecked] = useState([]);
  const [left, setLeft] = useState([
    "Food",
    "Attraction",
    "Public Transporation",
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
        <FormLabel component="legend">1. Select Your Room Type</FormLabel>
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
        </FormGroup>
        <FormLabel component="legend">2. Select Your Price Range</FormLabel>

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
      <Button variant="contained" onClick={handleSubmit}>
        Find!
      </Button>

      {
        airbnbList.map((airbnb) =>
          <Card sx={{width:1/1.5, maxWidth:500}}>
            <CardContent>
              <Stack direction="row" justifyContent="space-between">
                {/* <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
                  Word of the Day
                </Typography> */}
                <Typography variant="h5" component="div">
                  {airbnb.name}
                </Typography>
                <Typography variant="h5" component="div">
                  ${airbnb.price} CAD per night  / {airbnb.review_scores_rating}
                </Typography>
              </Stack>
              <Typography sx={{ mb: 1.5 }} color="text.secondary">
                {airbnb.listing_url}
              </Typography>
              <Typography variant="body2">
                {airbnb.name}
              </Typography>
            </CardContent>
          </Card>
        )

      }
    </Stack>
  );
}

export default App;
