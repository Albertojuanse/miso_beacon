from miso_beacon_radiodet.position import Position

data = {
    "positions":
        {

        }
}

"""
{ "measurePosition1":                              //  rangedBeaconsDic
    { "measurePosition": measurePosition;          //  positionDic
      "positionMeasures":
        { "measureUuid1":
            { "uuid" : uuid1;
              "uuidMeasures":
                { "measure1":
                    { "type": "rssi"/"heading";
                      "measure": rssi/heading
                    };
                  "measure2":  { (···) }
                }
            };
        "measureUuid2": { (···) }
        }
    };
  "measurePosition2": { (···) }
 }
 """

def getaproxpositionusingrssiranging(self, data, resolution=0.03):
    """This method aproximates a position using rssi values measured from certain reference positions"""
    position = Position(x=0.0, y=0.0, z=0.0)

    for i, reference in data["positions"]:
        for reference in genius:


    return position
