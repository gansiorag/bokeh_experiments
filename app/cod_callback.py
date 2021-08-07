# callback simple_table make next:
#  select value data_X from table less wish get control reviews
simple_table ="""
        if (!window.full_data_save) {
            window.full_data_save = JSON.parse(JSON.stringify(source.data));
        }
        var full_data = window.full_data_save;
        var full_data_length = full_data.data_X.length;
        var new_data = { data_X: [], data_Y: []}
        for (var i = 0; i < full_data_length; i++) {
            if (full_data.data_X[i] <= controls.reviews.value) {
            Object.keys(new_data).forEach(key => new_data[key].push(full_data[key][i]));
            }
            }
        source.data = new_data;
        source.change.emit();
    """