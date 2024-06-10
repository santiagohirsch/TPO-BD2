db.albums.aggregate([
    {
        $group: {
            _id: "$Year",
            count: { $sum: 1 }
        }
    },
    {
        $sort: { count: -1 }
    }
]).forEach(printjson);