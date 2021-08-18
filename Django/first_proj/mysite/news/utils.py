class MyMixin(object):
    mixin_prop = ''

    def get_prop(self):
        return self.mixin_prop.upper()

    def get_upper(self, st):
        if isinstance(st, str):
            return st.upper()
        else:
            # it is object
            return st.title.upper()
